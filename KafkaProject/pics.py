import os
import glob
folder_path = '/Users/rakireddy/Desktop/googlephotos/Takeout/GooglePhotos/marriage'
json_files = glob.glob(os.path.join(folder_path, '*.json'))
for file_path in json_files:
    os.remove(file_path)
    print(f"deleted: {file_path}")
