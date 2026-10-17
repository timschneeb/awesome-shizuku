#!/usr/bin/env python3
"""Generate site/data.js from README.md and pages/*.md."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site" / "data.js"

ITEM = re.compile(r"^(\s*)[*-] \[(?P<name>[^\]]+)\]\((?P<url>[^)\s]+)\)(?P<rest>.*)$")
SRC = re.compile(r"\s*\[\(Source code\)\]\((?P<url>[^)]+)\)")
LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")
TRIAL = re.compile(r"`(\d+-day trial)`")
LICENSE_TAGS = {"Paid", "IAP", "Ads", "Root"}


def clean(text):
    text = LINK.sub(r"\1", text)
    text = re.sub(r"\*\*|\*", "", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_item(m, section, group, kind):
    rest = m.group("rest")
    src = SRC.search(rest)
    source = src.group("url") if src else None
    rest = SRC.sub("", rest)
    tags = []
    for t in re.findall(r"`([^`]+)`", rest):
        if t in LICENSE_TAGS or TRIAL.match(f"`{t}`"):
            tags.append(t)
    featured = "✨" in rest
    ticks = [t for t in re.findall(r"`([^`]+)`", rest) if t not in tags]
    license_ = ticks[-1] if ticks else ""
    desc = rest
    desc = re.sub(r"`[^`]+`", "", desc).replace("✨", "").replace("💰", "")
    desc = desc.strip()
    desc = re.sub(r"^-\s*", "", desc)
    return {
        "name": m.group("name").strip(),
        "url": m.group("url"),
        "source": source,
        "desc": clean(desc),
        "license": license_,
        "tags": tags,
        "featured": featured,
        "kind": kind,
        "section": section,
        "group": group,
        "sub": len(m.group(1)) > 0,
    }


def parse(path, kind, top_levels):
    """top_levels maps an h2 title to a section label; h3/h4 become the group."""
    items, section, h3, group = [], None, None, None
    for line in path.read_text(encoding="utf-8").splitlines():
        h = re.match(r"^(#{2,4}) (.+?)\s*$", line)
        if h:
            level, title = len(h.group(1)), clean(h.group(2))
            if level == 2:
                section, h3, group = top_levels.get(title), None, None
            elif level == 3:
                h3 = group = title
            else:
                group = f"{h3} / {title}" if h3 else title
            continue
        if section is None:
            continue
        m = ITEM.match(line)
        if m:
            items.append(parse_item(m, section, group or section, kind))
    return items


LANGS = {"cn": ("README_cn.md", "CLOSED_SOURCE_cn.md", "RISH_cn.md"),
         "tw": ("README_tw.md", "CLOSED_SOURCE_tw.md", "RISH_tw.md")}
SECTIONS = {"Apps": "Apps", "Development libraries": "Development libraries",
            "Miscellaneous content": "Miscellaneous content"}


def main():
    items = []
    items += parse(ROOT / "README.md", "open", SECTIONS)
    items += parse(ROOT / "pages" / "CLOSED_SOURCE.md", "closed", {"Closed-source apps": "Apps"})
    items += parse(ROOT / "pages" / "ARCHIVED.md", "archived", {"Archived apps": "Apps"})
    rish = {"en": (ROOT / "pages" / "RISH.md").read_text(encoding="utf-8")}

    # Translations from the original project: match entries by (kind, URL) and
    # fall back to the English description when an entry is not translated.
    for lang, (readme, closed, rish_file) in LANGS.items():
        tr = parse(ROOT / readme, "open", SECTIONS)
        tr += parse(ROOT / "pages" / closed, "closed", {"Closed-source apps": "Apps", "Closed-source apps ": "Apps"})
        by_url = {}
        for t in tr:
            by_url.setdefault((t["kind"], t["url"]), []).append(t["desc"])
        for it in items:
            found = by_url.get((it["kind"], it["url"]))
            if found:
                it["desc_" + lang] = found.pop(0)
        rish[lang] = (ROOT / "pages" / rish_file).read_text(encoding="utf-8")
    payload = {"apps": items, "rish": rish}
    OUT.write_text("window.SHIZUKU_DATA = " + json.dumps(payload, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}: {len(items)} entries")


if __name__ == "__main__":
    main()
