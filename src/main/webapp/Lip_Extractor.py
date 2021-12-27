import os
import cv2
from imutils import face_utils
import numpy as np
import imutils
import dlib

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

vidcap = cv2.VideoCapture('test.mp4')
success, image = vidcap.read()
count = 0

# create new directory for frame
dirname = 'frame'
os.mkdir(dirname)

while success:

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale image
    rects = detector(gray, 1)
    for (i, rect) in enumerate(rects):
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
            if name == 'mouth':
                # h,w modify
                (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
                max_value = max(h, w)
                y = y - max_value // 3
                roi = image[y:y + max_value, x:x + max_value]
                roi = imutils.resize(roi, width=250, inter=cv2.INTER_CUBIC)

    cv2.imwrite(os.path.join(dirname, "frame-%d.jpg" % count), roi)  # save frame as JPEG file
    success, image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1
