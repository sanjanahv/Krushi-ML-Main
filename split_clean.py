import os
import shutil
import random

SRC = "dataset/clean"
OUT = "dataset"

SPLIT_RATIO = (0.7, 0.15, 0.15)
random.seed(42)

# Create output folders
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(OUT, split), exist_ok=True)

# Loop through each class
for cls in os.listdir(SRC):
    cls_path = os.path.join(SRC, cls)
    if not os.path.isdir(cls_path):
        continue

    images = os.listdir(cls_path)
    random.shuffle(images)

    total = len(images)
    train_end = int(total * SPLIT_RATIO[0])
    val_end = int(total * (SPLIT_RATIO[0] + SPLIT_RATIO[1]))

    splits = {
        "train": images[:train_end],
        "val": images[train_end:val_end],
        "test": images[val_end:]
    }

    for split_name, files in splits.items():
        split_cls_path = os.path.join(OUT, split_name, cls)
        os.makedirs(split_cls_path, exist_ok=True)

        for file in files:
            src_file = os.path.join(cls_path, file)
            dst_file = os.path.join(split_cls_path, file)
            shutil.copy(src_file, dst_file)

print("Re-split completed successfully.")
