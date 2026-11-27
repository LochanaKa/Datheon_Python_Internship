
import os
import shutil
from pathlib import Path

SOURCE_FOLDER = "test_files"

FILE_TYPES = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".webp": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",

    ".py": "Code",
    ".java": "Code",
    ".cpp": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code",
    ".sql": "Code"
}


def create_category_folders():
    categories = set(FILE_TYPES.values())
    categories.add("Others")

    for category in categories:
        folder_path = Path(SOURCE_FOLDER) / category
        folder_path.mkdir(parents=True, exist_ok=True)


def move_files():
    moved = 0
    skipped = 0

    print("\nStarting file organization...")
    print("-" * 40)

    with os.scandir(SOURCE_FOLDER) as files:
        for file in files:

            if not file.is_file():
                continue

            source_path = Path(file.path)

            extension = source_path.suffix.lower()
            category = FILE_TYPES.get(extension, "Others")

            destination_folder = Path(SOURCE_FOLDER) / category
            destination_path = destination_folder / source_path.name

            # Avoid overwriting existing files
            if destination_path.exists():
                print(f"Skipped: {source_path.name} (already exists)")
                skipped += 1
                continue

            shutil.move(str(source_path), str(destination_path))

            print(f"Moved: {source_path.name} -> {category}")
            moved += 1

    print("\n" + "=" * 40)
    print("FILE ORGANIZATION SUMMARY")
    print("=" * 40)
    print("Successfully moved:", moved)
    print("Skipped:", skipped)
    print("Total:", moved + skipped)
    print("=" * 40)


if __name__ == "__main__":
    create_category_folders()
    move_files()
