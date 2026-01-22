import os, cv2

SRC = "dataset/raw"
DST = "dataset/clean"
SIZE = (224, 224)

os.makedirs(DST, exist_ok=True)

for cls in os.listdir(SRC):
    src_cls = os.path.join(SRC, cls)
    if not os.path.isdir(src_cls):
        continue

    dst_cls = os.path.join(DST, cls)
    os.makedirs(dst_cls, exist_ok=True)

    for img in os.listdir(src_cls):
        img_path = os.path.join(src_cls, img)
        if not os.path.isfile(img_path):
            continue

        image = cv2.imread(img_path)
        if image is None:
            continue

        image = cv2.resize(image, SIZE)
        cv2.imwrite(os.path.join(dst_cls, img), image)

print("Resizing done successfully.")
