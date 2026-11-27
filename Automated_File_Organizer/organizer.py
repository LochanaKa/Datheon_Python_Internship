
import os
from pathlib import Path

# Define source directory
SOURCE_FOLDER = "test_files"


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


if __name__ == "__main__":
    inspect_files()
