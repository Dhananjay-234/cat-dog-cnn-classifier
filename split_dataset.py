import os
import shutil
import random

SOURCE_DIR = r"D:\brave\archive\PetImages"
DEST_DIR = r"D:\brave\archive\PetImages_Split"
TRAIN_RATIO = 0.8

mapping = {
    "Cat": "cats",
    "Dog": "dogs"
}

for src_name, dst_name in mapping.items():
    src_path = os.path.join(SOURCE_DIR, src_name)

    train_path = os.path.join(DEST_DIR, "train", dst_name)
    val_path = os.path.join(DEST_DIR, "validation", dst_name)

    os.makedirs(train_path, exist_ok=True)
    os.makedirs(val_path, exist_ok=True)

    images = os.listdir(src_path)
    images = [img for img in images if img.lower().endswith(('.jpg', '.png', '.jpeg'))]

    random.shuffle(images)

    split = int(len(images) * TRAIN_RATIO)
    train_images = images[:split]
    val_images = images[split:]

    for img in train_images:
        shutil.copy(os.path.join(src_path, img), os.path.join(train_path, img))

    for img in val_images:
        shutil.copy(os.path.join(src_path, img), os.path.join(val_path, img))

    print(f"{dst_name}: {len(train_images)} train | {len(val_images)} validation")

print("✅ Dataset successfully split into train & validation folders")
