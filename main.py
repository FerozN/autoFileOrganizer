import os
import shutil
import json

def organize_files(config):
    input_path = config["input_path"]
    output_path = config["output_path"]

    files = os.listdir(input_path)

    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(os.path.join(output_path, extension)):
            shutil.move(os.path.join(input_path, file), os.path.join(output_path, extension, file))
        else:
            os.makedirs(os.path.join(output_path, extension))
            shutil.move(os.path.join(input_path, file), os.path.join(output_path, extension, file))

if __name__ == "__main__":
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    organize_files(config)
