import os
import re

root_dir = input("Root directory: ").strip()

old_creator = input("Creator to rename: ").strip()
new_creator = input("New creator name (leave blank to remove): ").strip()

renamed = 0

for root, dirs, files in os.walk(root_dir):
    for filename in files:

        match = re.match(
            rf"^(.*?)\s*\({re.escape(old_creator)}\)(\.[^.]+)$",
            filename,
            re.IGNORECASE
        )

        if not match:
            continue

        game_name = match.group(1)
        extension = match.group(2)

        if new_creator:
            new_filename = f"{game_name} ({new_creator}){extension}"
        else:
            new_filename = f"{game_name}{extension}"

        old_path = os.path.join(root, filename)
        new_path = os.path.join(root, new_filename)

        print(f"Renaming:")
        print(f"  {filename}")
        print(f"  -> {new_filename}")

        os.rename(old_path, new_path)
        renamed += 1

print(f"\nDone. Renamed {renamed} file(s).")
