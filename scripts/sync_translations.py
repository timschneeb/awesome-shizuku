import re
from collections import defaultdict

def sync_readme(source_path, target_path, toc_heading, source_code_label):
    # Chinese Parser: Very lenient to catch broken formatting
    # Just looks for [Name](URL) and grabs everything after it.
    cn_app_pattern = re.compile(r'^(\s*(?:\*|-)\s+)\[([^\]]+)\]\(([^)]+)\)(.*)$')
    cn_end_stripper = re.compile(r'(?:\s*`[^`]+`|\s*\[\(.*?\)\]\(.*?\)|\s*💰|\s*✨|\s*-\s*)+$')
    cn_front_stripper = re.compile(r'^(?:\s*`[^`]+`|\s*💰|\s*✨|\s*-\s*)+')

    # English Parser: Strict 
    # Requires spaces around the hyphen (\s+-\s+) so it doesn't break tags like '15-day trial'
    en_app_pattern = re.compile(r'^(\s*(?:\*|-)\s+)\[([^\]]+)\]\(([^)]+)\)(.*?)\s+-\s+(.*)$')
    en_end_stripper = re.compile(r'(?:\s*`[^`]+`|\s*\[\(.*?\)\]\(.*?\)|\s*💰|\s*✨)+$')

    with open(source_path, 'r', encoding='utf-8') as f:
        source_lines = f.read().splitlines()
    with open(target_path, 'r', encoding='utf-8') as f:
        target_lines = f.read().splitlines()

    translations_by_url = {}
    translations_by_name = {}
    annotations_map = {}
    target_info_boxes = defaultdict(list)
    subpoint_translations = defaultdict(list)

    pre_toc_block = []
    unlisted_block = []
    license_block = []

    current_section = "PRE_TOC"
    current_header = "PRE_TOC"
    current_parent_url = None
    current_info_box = []

    # --- Parse translated file ---
    for line in target_lines:
        if line.startswith('## ') or line.startswith('### '):
            current_header = line.strip()

        if line.startswith(toc_heading):
            current_section = "TOC"
            continue
        elif line.startswith('### Unlisted apps'):
            current_section = "UNLISTED"
            unlisted_block.append(line)
            continue
        elif line.startswith('## License'):
            current_section = "LICENSE"
            license_block.append(line)
            continue
        elif line.startswith('## Annotations'):
            current_section = "ANNOTATIONS"
            continue

        if current_section == "UNLISTED" and line.startswith('## '): current_section = "CONTENT"
        elif current_section == "TOC" and line.startswith('## '): current_section = "CONTENT"

        if current_section == "PRE_TOC":
            pre_toc_block.append(line)
        elif current_section == "UNLISTED":
            unlisted_block.append(line)
        elif current_section == "LICENSE":
            license_block.append(line)
        elif current_section == "ANNOTATIONS":
            m = re.match(r'^(\s*(?:\*|-)\s+)(.*?)\s+-\s+(.*)$', line)
            if m: annotations_map[m.group(2).strip()] = m.group(3)
        elif current_section == "CONTENT":
            if line.startswith('>'):
                current_info_box.append(line)
                continue
            elif current_info_box:
                target_info_boxes[current_header].append('\n'.join(current_info_box))
                current_info_box = []

            m = cn_app_pattern.match(line)
            if m:
                bullet, name, url, remainder = m.groups()
                # Clean up the Chinese translation using the strippers
                pure_desc = cn_end_stripper.sub('', remainder).strip()
                pure_desc = cn_front_stripper.sub('', pure_desc).strip()

                url_clean = url.strip()
                translations_by_url[url_clean] = pure_desc
                translations_by_name[name.strip().lower()] = pure_desc
                current_parent_url = url_clean
            elif line.startswith(' ') or line.startswith('\t'):
                if current_parent_url:
                    subpoint_translations[current_parent_url].append(line)
            else:
                current_parent_url = None

    # --- Parse English file ---
    output_lines = []
    output_lines.extend(pre_toc_block)

    current_source_section = "PRE_TOC"
    current_source_header = "PRE_TOC"
    current_source_parent_url = None
    subpoint_counters = defaultdict(int)
    in_english_info_box = False

    for line in source_lines:
        if line.startswith('## ') or line.startswith('### '):
            current_source_header = line.strip()

        if line.startswith('## Table of contents'):
            current_source_section = "TOC"
            output_lines.append(toc_heading)
            continue
        elif line.startswith('### Unlisted apps'):
            current_source_section = "UNLISTED"
            output_lines.extend(unlisted_block)
            continue
        elif line.startswith('## License'):
            current_source_section = "LICENSE"
            output_lines.extend(license_block)
            continue
        elif line.startswith('## Annotations'):
            current_source_section = "ANNOTATIONS"
            output_lines.append(line)
            continue

        if current_source_section == "UNLISTED" and line.startswith('## '): current_source_section = "CONTENT"
        elif current_source_section == "TOC" and line.startswith('## '): current_source_section = "CONTENT"

        if current_source_section in ["PRE_TOC", "UNLISTED", "LICENSE"]: continue
        elif current_source_section == "TOC": output_lines.append(line)
        elif current_source_section == "ANNOTATIONS":
            m = re.match(r'^(\s*(?:\*|-)\s+)(.*?)\s+-\s+(.*)$', line)
            if m:
                tag = m.group(2).strip()
                output_lines.append(f"{m.group(1)}{tag} - {annotations_map.get(tag, m.group(3))}")
            else: output_lines.append(line)
        elif current_source_section == "CONTENT":
            if line.startswith('>'):
                if not in_english_info_box:
                    in_english_info_box = True
                    if target_info_boxes.get(current_source_header):
                        output_lines.append(target_info_boxes[current_source_header].pop(0))
                continue
            else: in_english_info_box = False

            m = en_app_pattern.match(line)
            if m:
                # The Strict English Parser safely extracts Pre-Tags
                bullet, name, url, tags_pre, remainder = m.groups()
                current_source_parent_url = url.strip()

                # Separate Description from Post-Tags
                tags_m = en_end_stripper.search(remainder)
                tags_post = tags_m.group(0) if tags_m else ""
                en_desc = remainder[:-len(tags_post)].strip() if tags_post else remainder.strip()

                # Translate "Source code" label
                tags_post = re.sub(r'\(Source code\)', f'({source_code_label})', tags_post, flags=re.IGNORECASE)

                # Retrieve translation
                trans = translations_by_url.get(current_source_parent_url) or \
                        translations_by_name.get(name.strip().lower()) or en_desc

                # Reassemble with Pre-Tags intact!
                output_lines.append(f"{bullet}[{name}]({url}){tags_pre} - {trans}{tags_post}")

            elif (line.startswith(' ') or line.startswith('\t')) and current_source_parent_url:
                # Handle non-standard subpoints (like plain text notes)
                idx = subpoint_counters[current_source_parent_url]
                existing_subs = subpoint_translations.get(current_source_parent_url, [])

                if idx < len(existing_subs):
                    output_lines.append(existing_subs[idx])
                else:
                    output_lines.append(line)
                subpoint_counters[current_source_parent_url] += 1
            else:
                current_source_parent_url = None
                output_lines.append(line)

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines) + '\n')
    print(f"Synced: {target_path}")

if __name__ == "__main__":
    sync_readme('../README.md', 'README_cn.md', '## 目录', '源代码')
    sync_readme('../README.md', 'README_tw.md', '## 目錄', '原始碼')