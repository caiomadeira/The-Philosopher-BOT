import os
from Images.reference import IMG_PATH
for root, dirs, files in os.walk(IMG_PATH):
    for file in files:
        if file.endswith(".png"):
             print(os.path.join(root, file))