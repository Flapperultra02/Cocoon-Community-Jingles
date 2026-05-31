import os
import json
import re

ROOT_DIR = "jingles"
COLLECTION_NAME = "Cocoon Coummunity Jingles"

AUDIO_EXTENSIONS = {".ogg", ".mp3", ".wav", ".flac", ".m4a"}

data = {
    "name": COLLECTION_NAME
}


def make_regex(name):
    # Remove extension
    name = os.path.splitext(name)[0]

    # Escape special regex chars
    parts = re.findall(r"[a-zA-Z0-9]+", name.lower())

    if not parts:
        return "^$"

    # Allow punctuation/spaces between words
    regex = "^" + r"[^a-z0-9]*".join(parts) + "$"

    # Also allow fully condensed version
    condensed = "^" + "".join(parts) + "$"

    return f"{regex}|{condensed}"


for platform in sorted(os.listdir(ROOT_DIR)):
    platform_path = os.path.join(ROOT_DIR, platform)

    if not os.path.isdir(platform_path):
        continue

    entries = []

    for file in sorted(os.listdir(platform_path)):
        ext = os.path.splitext(file)[1].lower()

        if ext not in AUDIO_EXTENSIONS:
            continue

        display_name = os.path.splitext(file)[0]
        display_name = re.sub(r"\s*\([^)]*\)\s*$", "", display_name)

        entries.append({
            "name": display_name,
            "file": f"jingles/{platform}/{file}",
            "regex": make_regex(display_name)
        })

    data[platform] = entries

with open("jingles.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Generated jingles.json")
