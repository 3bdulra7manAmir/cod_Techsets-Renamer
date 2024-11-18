import os

def rename_files(directory):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    for filename in os.listdir(directory):
        if "__iw6" in filename:
            old_filepath = os.path.join(directory, filename)
            new_filename = filename.replace("__iw6", "_iw6")
            new_filepath = os.path.join(directory, new_filename)

            try:
                if not os.path.exists(new_filepath):
                    os.rename(old_filepath, new_filepath)
                    log_message(f"Renamed: {filename} -> {new_filename}")
                else:
                    log_message(f"Skipped: {filename} (Target {new_filename} already exists)")
            except Exception as e:
                log_message(f"Error renaming {filename}: {e}")

def log_message(message):
    log_file = "rename_log.txt"
    with open(log_file, 'a') as log:
        log.write(message + "\n")

# Main execution
if __name__ == "__main__":
    directory_path = "E:\\h2\\zonetool\\iw6_test\\techsets\\ps"
    try:
        rename_files(directory_path)
        print(f"File renaming completed for directory: {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
