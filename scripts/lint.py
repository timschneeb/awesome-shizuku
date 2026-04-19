import os
import re
import sys

def lint_readme(file_path):
    app_pattern = re.compile(r'^(\s*(?:\*|-)\s+)\[([^\]]+)\]\(([^)]+)\)(.*?)\s+-\s+(.*)$')
    entry_start_pattern = re.compile(r'^\s*(?:\*|-)\s+\[[^\]]+\]\([^)]+\)')
    end_pattern = re.compile(r'^(.*?)\s+`([^`]+)`(?:\s+\[\(Source code\)\]\(([^)]+)\))?\s*$')

    valid_tags_patterns = [
        r'`Paid`\s*💰?',
        r'`IAP`\s*💰?',
        r'`Ads`',
        r'`\d+-\w+ trial`\s*💰?',
        r'`Root`\s*💰?',
        r'✨'
    ]

    errors = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_content_section = False

    for i, line in enumerate(lines):
        line_num = i + 1
        line_stripped = line.strip()

        if line_stripped.startswith('## Table of contents'):
            in_content_section = False
            continue

        if re.match(r'^#{2,6}\s+', line_stripped):
            current_category = line_stripped.replace('#', '').strip()

            if current_category not in ["License", "Annotations", "Languages", "Table of contents"]:
                in_content_section = True
            else:
                in_content_section = False
            continue

        if not in_content_section:
            continue

        match = app_pattern.match(line)
        if match:
            indent, name, url, pre_tags, remainder = match.groups()

            # --- Validating Pre-Tags ---
            if pre_tags.strip():
                leftover_tags = pre_tags
                for pattern in valid_tags_patterns:
                    leftover_tags = re.sub(pattern, '', leftover_tags)

                leftover_tags = leftover_tags.strip()
                if leftover_tags:
                    errors.append(f"[Line {line_num}] INVALID TAG: Unrecognized tag or spacing issue before the hyphen: '{pre_tags.strip()}'. ({name})")

            # --- Validating Description, License, and Source Link ---
            end_match = end_pattern.match(remainder)
            if not end_match:
                errors.append(f"[Line {line_num}] MALFORMED ENDING: App must end with an SPDX `License` tag, optionally followed by [(Source code)](...). ({name})")
            else:
                desc_only, license_tag, source_url = end_match.groups()
                desc_clean = desc_only.strip()

                if desc_clean.endswith('-'):
                    errors.append(f"[Line {line_num}] EXTRA HYPHEN: Remove the stray hyphen before the license tag. ({name})")
                if '[(Source code)]' in desc_clean:
                    errors.append(f"[Line {line_num}] WRONG TAG ORDER: The `License` tag must come before the [(Source code)] link. ({name})")

                # Length check
                if len(desc_clean) >= 250:
                    errors.append(f"[Line {line_num}] DESCRIPTION TOO LONG: {len(desc_clean)} chars. Max is 250. ({name})")

                # Duplicate link check
                if source_url and source_url.strip() == url.strip():
                    errors.append(f"[Line {line_num}] DUPLICATE LINK: The '(Source code)' link is identical to the main URL. Remove the source code link. ({name})")

        else:
            if entry_start_pattern.match(line):
                errors.append(f"[Line {line_num}] MALFORMED ENTRY: Ensure the entry exactly matches '* [Name](URL) [Tags] - Description'. Missing hyphen? ({line_stripped[:40]}...)")

    # --- Generate GitHub Actions Summary ---
    summary_file = os.environ.get('GITHUB_STEP_SUMMARY')

    if not errors:
        print(f"Linting passed for {file_path}")
        if summary_file:
            with open(summary_file, 'a', encoding='utf-8') as f:
                f.write(f"### ✅ {file_path}\n\n\n")
        return True
    else:
        print(f"❌ Found {len(errors)} formatting error(s) in {file_path}:\n")
        for e in errors:
            print(e)

        if summary_file:
            with open(summary_file, 'a', encoding='utf-8') as f:
                f.write(f"### ❌ {file_path}\nFound **{len(errors)}** formatting error(s):\n\n")
                for e in errors:
                    f.write(f"- {e}\n")
                f.write("\n---\n")
        return False

if __name__ == "__main__":
    success_readme = lint_readme('README.md')
    success_archived = lint_readme('pages/ARCHIVED.md')

    if not success_readme or not success_archived:
        sys.exit(1)
    else:
        sys.exit(0)