import os
import shutil


def read_log(log_file):
    if not os.path.isfile(log_file):
        raise FileNotFoundError(f"Log file '{log_file}' does not exist.")

    try:
        with open(log_file, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        raise RuntimeError(f"Error reading log file: {e}")


def copy_file(file_name, source_dir, dest_dir):
    source_path = os.path.join(source_dir, file_name)
    dest_path = os.path.join(dest_dir, file_name)

    if not os.path.isfile(source_path):
        log_error(f"Source file not found: {source_path}")
        return False

    try:
        shutil.copyfile(source_path, dest_path)
        return True
    except Exception as e:
        log_error(f"Failed to copy '{file_name}': {e}")
        return False


def log_error(message):
    log_file = "copy_error_log.txt"
    try:
        with open(log_file, 'a') as log:
            log.write(message + "\n")
    except Exception as e:
        print(f"Failed to write to error log: {e}")


def validate_directory(path, dir_type="directory"):
    if not os.path.isdir(path):
        print(f"{dir_type.capitalize()} directory '{path}' does not exist.")
        return False
    return True


def main():
    source_dir = input("Enter the source directory: ").strip()
    dest_dir = input("Enter the destination directory: ").strip()
    log_file = input("Enter the log file: ").strip()

    # Validate directories
    if not validate_directory(source_dir, "source") or not validate_directory(dest_dir, "destination"):
        return

    try:
        file_names = read_log(log_file)
    except Exception as e:
        print(f"Error reading log file: {e}")
        return

    success_count = 0
    failure_count = 0

    for file_name in file_names:
        if copy_file(file_name, source_dir, dest_dir):
            print(f"Copied: {file_name}")
            success_count += 1
        else:
            print(f"Skipped: {file_name}")
            failure_count += 1

    # Summary
    print(f"\nCopy process completed. Files copied: {success_count}, Files failed: {failure_count}")


if __name__ == "__main__":
    main()
