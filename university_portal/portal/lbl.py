import cv2
import os
import numpy as np
import pickle
from PIL import Image


def label():
    y_lable = []
    x_train = []

    face_haar_cascade = cv2.CascadeClassifier(
        '/Users/DELL/Desktop/university_portal/cascades/data/haarcascade_frontalface_default.xml')
    reccognizer = cv2.face.LBPHFaceRecognizer_create()
    bace_dir = os.path.dirname(os.path.abspath((__file__)))
    imd_dir = os.path.join(bace_dir, "train")
    current_id = 0
    lable_id = {}
    for root, dir, files in os.walk(imd_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                lable = os.path.basename(root).replace(" ", "-").lower()
                # print(lable,path)
                if not lable in lable_id:
                    lable_id[lable] = current_id
                    current_id = current_id + 1
                id_ = lable_id[lable]
                # x_train.append(path)
                # y_lable.append(lable)
                pil_img = Image.open(path).convert("L")  # grayscale
                size = (550, 550)
                final_img = pil_img.resize(size, Image.ANTIALIAS)
                img_array = np.array(pil_img, "uint8")
                # print(img_array)
                faces = face_haar_cascade.detectMultiScale(img_array, minNeighbors=5)

                for (x, y, w, h) in faces:
                    roi = img_array[y:y + h, x:x + w]
                    x_train.append(roi)
                    y_lable.append(id_)

    with open("/Users/DELL/Desktop/university_portal/labes.pickle", "wb") as f:
        pickle.dump(lable_id, f)

    reccognizer.train(x_train, np.array(y_lable))
    reccognizer.save("/Users/DELL/Desktop/university_portal/trainner.yml")
