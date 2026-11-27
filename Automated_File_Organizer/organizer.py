
import os

# Define the source directory
SOURCE_FOLDER = "test_files"


def inspect_files():

    print("Scanning directory...")
    print("-" * 30)

    with os.scandir(SOURCE_FOLDER) as files:

        for file in files:

            if file.is_file():

                print("File:", file.name)


if __name__ == "__main__":
    inspect_files()
