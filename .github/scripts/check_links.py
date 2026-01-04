#!/usr/bin/env python3
import re
import os
import requests
from datetime import datetime, timedelta

def get_github_token():
    """Gets the GitHub token from the environment variables."""
    return os.environ.get("GITHUB_TOKEN")

def extract_github_repos(text):
    """Extracts unique GitHub repository paths from a given text."""
    # This regex is designed to capture user/repo from various GitHub URL formats
    pattern = r"https://github\.com/([\w.-]+/[\w.-]+)"
    matches = re.findall(pattern, text)
    # Filter out common non-repo paths
    non_repo_paths = {
        'sindresorhus/awesome', 
        'timschneeb/changelog-awesome-shizuku',
        'RikkaApps/Shizuku-API', 
    }
    # Use a set for efficiency and to store unique repository paths
    unique_repos = {repo for repo in matches if repo not in non_repo_paths}
    return sorted(list(unique_repos)) # Return a sorted list for consistent processing order

def get_repo_info(repo_path, token):
    """
    Fetches repository information from the GitHub API.
    Returns a dictionary with 'archived' status and 'pushed_at' date, or None on error.
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

        return {
            "name": repo_data.get("full_name", repo_path),
            "archived": repo_data.get("archived", False),
            "pushed_at": pushed_at_date,
            "url": repo_data.get("html_url", f"https://github.com/{repo_path}")
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
    github_token = get_github_token()
    if not github_token:
        print("Warning: GITHUB_TOKEN environment variable not set. Using unauthenticated requests, which have a lower rate limit.")

    try:
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()
    except FileNotFoundError:
        print("Error: README.md not found in the current directory.")
        return

    repo_paths = extract_github_repos(readme_content)
    print(f"Found {len(repo_paths)} unique GitHub repositories to check.")

    archived_repos = []
    inactive_repos = []
    time_limit = datetime.now(datetime.now().astimezone().tzinfo) - timedelta(days=2*365)

    for repo_path in repo_paths:
        print(f"Checking {repo_path}...")
        info = get_repo_info(repo_path, github_token)
        
        if info:
            if info["archived"]:
                archived_repos.append(info)
            
            if info["pushed_at"] < time_limit:
                inactive_repos.append(info)

    # Sort inactive repositories by last commit date, descending
    inactive_repos.sort(key=lambda x: x["pushed_at"], reverse=True)

    # Generate the markdown report
    with open("report.md", "w", encoding="utf-8") as f:
        f.write("# GitHub Repository Status Report\n\n")
        f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Archived Repositories\n\n")
        if archived_repos:
            f.write("| Repository | Last Push |\n")
            f.write("|------------|-----------|\n")
            for repo in sorted(archived_repos, key=lambda x: x['pushed_at'], reverse=True):
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

    print("\nReport generated successfully: report.md")

if __name__ == "__main__":
    main()
