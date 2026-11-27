
import os
from pathlib import Path

# Define source directory
SOURCE_FOLDER = "test_files"

# Extension and category mapping
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


def inspect_files():

    print("Scanning directory...")
    print("-" * 40)

    with os.scandir(SOURCE_FOLDER) as files:

        for file in files:

            if file.is_file():

                file_path = Path(file.name)

                extension = file_path.suffix.lower()

                print("File:", file.name)
                print("Extension:", extension)
                print("-" * 40)

def create_category_folders():

    categories = set(FILE_TYPES.values())
    categories.add("Others")

    print("\nCreating category folders...")

    for category in categories:

        folder_path = os.path.join(SOURCE_FOLDER, category)

        os.makedirs(folder_path, exist_ok=True)

        print("Created/verified:", category)

if __name__ == "__main__":
    inspect_files()
    create_category_folders()
