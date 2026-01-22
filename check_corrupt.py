import os, cv2

DATA_DIR = "."
bad = 0

for cls in os.listdir(DATA_DIR):
    cls_path = os.path.join(DATA_DIR, cls)
    if not os.path.isdir(cls_path):
        continue

    for img in os.listdir(cls_path):
        img_path = os.path.join(cls_path, img)
        image = cv2.imread(img_path)
        if image is None:
            os.remove(img_path)
            bad += 1

print("Deleted corrupted images:", bad)
