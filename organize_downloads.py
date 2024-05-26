import os
import logging
import yaml

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def organize_file(filename, config, downloads_folder):
    file_extension = os.path.splitext(filename)[1].lower()
    for folder_name, extensions in config['folders'].items():
        if file_extension in extensions or (folder_name == 'Apps' and filename.endswith('.app')):
            move_file(filename, folder_name, downloads_folder)
            break

def move_file(filename, folder_name, downloads_folder):
    folder_path = os.path.join(downloads_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    source = os.path.join(downloads_folder, filename)
    destination = os.path.join(folder_path, filename)

    # handle file naming conflicts
    base, extension = os.path.splitext(filename)
    counter = 1
    while os.path.exists(destination):
        new_filename = f"{base} ({counter}){extension}"
        destination = os.path.join(folder_path, new_filename)
        counter += 1

    os.rename(source, destination)
    logging.info(f"Moved: {filename} to {folder_name}")

if __name__ == "__main__":
    downloads_folder = os.path.expanduser("~/Downloads")
    config_path = 'config.yaml'
    config = load_config(config_path)

    logging.info("Starting to organize the Downloads folder.")

    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(file_path) or filename.endswith('.app'):
            organize_file(filename, config, downloads_folder)

    logging.info("Finished organizing.")