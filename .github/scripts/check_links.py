#!/usr/bin/env python3
import re
import os
import requests
from datetime import datetime, timedelta

def get_github_token():
    """Gets the GitHub token from the environment variables."""
    return os.environ.get("GITHUB_TOKEN")

def extract_repo_details(text):
    """Extracts unique GitHub repository paths and their declared licenses from a given text."""
    repo_details = {}
    
    # Regex for GitHub repo paths
    repo_pattern = r"https://github\.com/([\w.-]+/[\w.-]+)"
    # Regex for tags in backticks
    tag_pattern = r"`([^`]+)`"

    non_repo_paths = {
        'sindresorhus/awesome', 
        'timschneeb/changelog-awesome-shizuku',
        'RikkaApps/Shizuku-API', 
    }

    for line in text.splitlines():
        if not line.strip().startswith('*'):
            continue
        
        repo_matches = re.findall(repo_pattern, line)
        if not repo_matches:
            continue
        
        # Determine the primary repo for the line
        repo_path = None
        source_link_match = re.search(r"\[\(Source code\)\]\((https://github\.com/([\w.-]+/[\w.-]+))\)", line)
        if source_link_match:
            repo_path = source_link_match.group(2)
        else:
            # Take the first github link if no explicit "Source code"
            for match in repo_matches:
                if match not in non_repo_paths:
                    repo_path = match
                    break
        
        if not repo_path or repo_path in non_repo_paths:
            continue
        
        if repo_path in repo_details:
            continue # Already processed

        # Extract declared license
        declared_license = None
        tags = re.findall(tag_pattern, line)
        for tag in tags:
            # Heuristic for what constitutes a license string
            if any(kw in tag for kw in ['GPL', 'MPL', 'Apache', 'MIT', 'BSD', 'LGPL', 'AGPL', 'CC', 'OSL', 'Unlicense']) or tag in ['Proprietary', 'Propietary']:
                declared_license = tag
                if declared_license == 'Propietary':
                    declared_license = 'Proprietary'
                break
        
        repo_details[repo_path] = {
            "path": repo_path,
            "declared_license": declared_license
        }
        
    return sorted(repo_details.values(), key=lambda x: x['path'])

def get_repo_info(repo_path, token):
    """
    Fetches repository information from the GitHub API.
    Returns a dictionary with repo info, or None on error.
    """
    api_url = f"https://api.github.com/repos/{repo_path}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"
    
    try:
        response = requests.get(api_url, headers=headers)
        
        # Check for rate limiting
        if response.status_code == 403 and 'rate limit' in response.text.lower():
            print("GitHub API rate limit exceeded. Please try again later or use a GITHUB_TOKEN.")
            return None
            
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)
        
        repo_data = response.json()
        pushed_at_date = datetime.fromisoformat(repo_data["pushed_at"].replace("Z", "+00:00"))

        license_info = repo_data.get("license")
        actual_license = None
        if license_info and license_info.get("spdx_id") != "NOASSERTION":
            actual_license = license_info.get("spdx_id")

        return {
            "name": repo_data.get("full_name", repo_path),
            "archived": repo_data.get("archived", False),
            "pushed_at": pushed_at_date,
            "url": repo_data.get("html_url", f"https://github.com/{repo_path}"),
            "license": actual_license
        }
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Repository not found (404): {repo_path}")
        else:
            print(f"Failed to fetch data for {repo_path}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching {repo_path}: {e}")
        return None

def main():
    """Main function to read README, check repos, and generate a report."""

    def are_licenses_consistent(declared, actual):
        # If None, GitHub likely failed to detect the license. Ignore this.
        if actual is None:
            return True
        
        if declared is None:
            return False

        norm_declared = declared.replace(' ', '-')
        if 'MODIFIED-' in norm_declared:
            norm_declared = norm_declared.replace('MODIFIED-', '')

        return actual.startswith(norm_declared)

    github_token = get_github_token()
    if not github_token:
        print("Warning: GITHUB_TOKEN environment variable not set. Using unauthenticated requests, which have a lower rate limit.")

    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()
    except FileNotFoundError:
        print("Error: README.md not found in the current directory.")
        return

    repo_details = extract_repo_details(readme_content)
    print(f"Found {len(repo_details)} unique GitHub repositories to check.")

    archived_repos = []
    inactive_repos = []
    license_inconsistencies = []
    time_limit = datetime.now(datetime.now().astimezone().tzinfo) - timedelta(days=2*365)

    for detail in repo_details:
        repo_path = detail['path']
        declared_license = detail['declared_license']
        
        print(f"Checking {repo_path}...")
        info = get_repo_info(repo_path, github_token)
        
        if info:
            if info["archived"]:
                archived_repos.append(info)
            
            if info["pushed_at"] < time_limit:
                inactive_repos.append(info)

            actual_license = info.get("license")
            if not are_licenses_consistent(declared_license, actual_license):
                license_inconsistencies.append({
                    "name": info["name"],
                    "url": info["url"],
                    "declared": declared_license or "(Not specified)",
                    "actual": actual_license, # Can't be null if inconsistent
                })


    # Sort repositories
    inactive_repos.sort(key=lambda x: x["pushed_at"], reverse=True)
    archived_repos.sort(key=lambda x: x['pushed_at'], reverse=True)
    license_inconsistencies.sort(key=lambda x: x['name'])


    # Generate the markdown report
    with open("report.md", "w", encoding="utf-8") as f:
        f.write("# GitHub Repository Status Report\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Archived Repositories\n\n")
        if archived_repos:
            f.write("| Repository | Last Push |\n")
            f.write("|------------|-----------|\n")
            for repo in archived_repos:
                f.write(f"| [{repo['name']}]({repo['url']}) | {repo['pushed_at'].strftime('%Y-%m-%d')} |\n")
        else:
            f.write("No archived repositories found.\n")
        f.write("\n")

        f.write("## Repositories Not Updated in the Last Two Years\n\n")
        if inactive_repos:
            f.write("| Repository | Last Push |\n")
            f.write("|------------|-----------|\n")
            for repo in inactive_repos:
                f.write(f"| [{repo['name']}]({repo['url']}) | {repo['pushed_at'].strftime('%Y-%m-%d')} |\n")
        else:
            f.write("No repositories found that haven't been updated in the last two years.\n")
        f.write("\n")
        
        f.write("## License Inconsistencies\n\n")
        if license_inconsistencies:
            f.write("| Repository | Declared in README | Detected on GitHub |\n")
            f.write("|------------|--------------------|--------------------|\n")
            for item in license_inconsistencies:
                f.write(f"| [{item['name']}]({item['url']}) | {item['declared']} | {item['actual']} |\n")
        else:
            f.write("No license inconsistencies found.\n")


    print("\nReport generated successfully: report.md")

if __name__ == "__main__":
    main()
