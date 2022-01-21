# import the necessary packages
from sklearn.metrics import mean_squared_error
from scipy.spatial import distance as dist

from imutils import face_utils
import numpy as np
import dlib
import cv2
import os


def mouth_aspect_ratio(mouth):
    # compute the euclidean distances between the two sets of
    # vertical mouth landmarks (x, y)-coordinates
    A = dist.euclidean(mouth[2], mouth[10])  # 51, 59
    B = dist.euclidean(mouth[4], mouth[8])  # 53, 57

    # compute the euclidean distance between the horizontal
    # mouth landmark (x, y)-coordinates
    C = dist.euclidean(mouth[0], mouth[6])  # 49, 55

    # compute the mouth aspect ratio
    mar = (A + B) / (2.0 * C)

    # return the mouth aspect ratio
    return mar


# grab the indexes of the facial landmarks for the mouth
(mStart, mEnd) = (49, 68)
marArray = []


def lip_extractor(video_path):
    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

    vidcap = cv2.VideoCapture(video_path)
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
            mouth = shape[mStart:mEnd]
            mouthMAR = mouth_aspect_ratio(mouth)
            mar = mouthMAR
            marArray.append(mar)
            print("frame:" + str(count) + "--mar_value:" + str(mar))
            for (name, (i, j)) in face_utils.FACIAL_LANDMARKS_IDXS.items():
                if name == 'mouth':
                    # h,w modify
                    (x, y, w, h) = cv2.boundingRect(np.array([shape[i:j]]))
                    max_value = max(h, w)
                    y = y - max_value // 3
                    roi = image[y:y + max_value, x:x + max_value]
                    roi = cv2.resize(roi, (250, 250))

        cv2.imwrite(os.path.join(dirname, "frame-%d.jpg" % count), roi)  # save frame as JPEG file
        success, image = vidcap.read()
        print('Read a new frame: ', success)
        count += 1


def compute_threshold():
    min_value = min(marArray)
    max_value = max(marArray)

    print("min_value" + str(min_value))
    print("max_value" + str(max_value))

    mean_value = (min_value + max_value) / 2

    print("mean_value" + str(mean_value))

    mean_array = []
    for i in range(0, len(marArray)):
        mean_array.append(mean_value)

    x = mean_squared_error(marArray, mean_array, squared=False)
    print(x)

    sum_v = mean_value - (x / 2)
    print(sum_v)
