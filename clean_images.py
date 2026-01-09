from PIL import Image
import os

def clean_folder(folder_path):
    removed = 0
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            img = Image.open(file_path)
            img.verify()
        except:
            os.remove(file_path)
            removed += 1
    print(f"Cleaned {folder_path} | Removed {removed} corrupted images")

base_dir = r"D:\brave\archive\PetImages_Split"

folders = [
    r"train\cats",
    r"train\dogs",
    r"validation\cats",
    r"validation\dogs"
]

for folder in folders:
    clean_folder(os.path.join(base_dir, folder))

print("✅ Image cleaning completed")
