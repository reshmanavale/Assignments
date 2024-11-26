import os
import shutil
import sys
import time

def backup_files(source_dir, dest_dir):
    """
    Backs up files from the source directory to the destination directory.
    If a file with the same name exists, appends a timestamp to the filename.

    :param source_dir: The source directory containing files to be backed up.
    :param dest_dir: The destination directory where files will be backed up.
    """
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        sys.exit(1)

    # Check if destination directory exists
    if not os.path.exists(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        sys.exit(1)

    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        
        # Skip directories
        if os.path.isdir(source_file):
            continue

        # Check if the file already exists in the destination directory
        dest_file = os.path.join(dest_dir, filename)
        
        if os.path.exists(dest_file):
            # If file exists, append timestamp to the filename
            base_name, ext = os.path.splitext(filename)
            timestamp = time.strftime("%Y%m%d%H%M%S")
            dest_file = os.path.join(dest_dir, f"{base_name}_{timestamp}{ext}")
            print(f"File '{filename}' already exists. Renaming to '{os.path.basename(dest_file)}'")

        # Copy the file to the destination directory
        try:
            shutil.copy2(source_file, dest_file)
            print(f"Successfully copied '{filename}' to '{dest_file}'")
        except Exception as e:
            print(f"Error copying file '{filename}': {e}")

def main():
    # Check if correct number of arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    # Get source and destination directories from command-line arguments
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    # Perform the backup
    backup_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()
