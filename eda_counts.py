import os
import matplotlib.pyplot as plt

DATA_DIR = "dataset/raw"

classes = []
counts = []

for cls in os.listdir(DATA_DIR):
    path = os.path.join(DATA_DIR, cls)
    if os.path.isdir(path):
        classes.append(cls)
        counts.append(len(os.listdir(path)))

plt.figure(figsize=(10,5))
plt.bar(classes, counts)
plt.xticks(rotation=90)
plt.ylabel("Image Count")
plt.title("Class Distribution")
plt.tight_layout()
plt.show()

for c, n in zip(classes, counts):
    print(c, ":", n)
