import os
import shutil


def read_log(log_file):
    if not os.path.isfile(log_file):
        raise FileNotFoundError(f"Log file '{log_file}' does not exist.")

    with open(log_file, "r") as f:
        return [line.strip() for line in f if line.strip()]


def copy_file(file_name, source_dir, dest_dir):
    source_path = os.path.join(source_dir, file_name)
    dest_path = os.path.join(dest_dir, file_name)

    try:
        shutil.copyfile(source_path, dest_path)
        return True
    except Exception as e:
        log_error(f"Failed to copy '{file_name}': {e}")
        return False


def log_error(message):
    log_file = "copy_error_log.txt"
    with open(log_file, 'a') as log:
        log.write(message + "\n")


def main():
    source_dir = input("Enter the source directory: ").strip()
    dest_dir = input("Enter the destination directory: ").strip()
    log_file = input("Enter the log file: ").strip()

    if not os.path.isdir(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    if not os.path.isdir(dest_dir):
        print(f"Destination directory '{dest_dir}' does not exist.")
        return

    try:
        file_names = read_log(log_file)
    except Exception as e:
        print(f"Error reading log file: {e}")
        return

    for file_name in file_names:
        if copy_file(file_name, source_dir, dest_dir):
            print(f"Copied: {file_name}")
        else:
            print(f"Skipped: {file_name}")


if __name__ == "__main__":
    main()
