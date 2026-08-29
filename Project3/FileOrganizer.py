import os
import shutil

source_folder="source"
destination_folder="jpg_files"


for file in os.listdir(source_folder):
    if file.lower().endswith((".jpg", ".jpeg")):
        source_path=os.path.join(source_folder, file)
        destination_path=os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file}")

print("All JPG files have been moved successfully!")