import os
import cv2
import glob
import re
import numpy as np
import shutil
from skimage.metrics import structural_similarity as ssim


def delete(filename1):
    os.remove(filename1)


def remove_image():
    dir_name = 'frame/'
    # Get list of all files in a given directory
    list_of_files = glob.glob(dir_name + '*')
    # sort all files numerically
    list_of_files.sort(key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
    img_n = []

    for currIndex, filename in enumerate(list_of_files):
        if not os.path.exists(list_of_files[currIndex]):
            print('not exist', list_of_files[currIndex])
            break
        img = cv2.imread(list_of_files[currIndex])
        img1 = cv2.imread(list_of_files[currIndex + 1])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        s = ssim(img, img1)

        img_n.append([list_of_files[currIndex], list_of_files[currIndex + 1], s])

        '''
        if s > 0.8:
            imgs_n.append(list_of_files[currIndex + 1])
            print(list_of_files[currIndex], list_of_files[currIndex + 1], s)
        else:
            print('small_ssim',list_of_files[currIndex],list_of_files[currIndex + 1], s)
        '''
        currIndex += 1

        if currIndex >= len(list_of_files) - 1:
            break

    data = np.array(img_n)
    data = data[np.argsort(data[:, 2])[::-1]]
    print(data)
    data = data[: -48]

    for current, file in enumerate(data):
        delete(data[current][0])
        current += 1




def replicate_last(num_frames):

    dir_name = 'frame/'
    list_of_files = glob.glob(dir_name + '*')
    list_of_files.sort(key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
    last_path = list_of_files[-1]
    last_path_number = last_path[-6:-4]

    num_repl = 49 - num_frames

    if num_repl > 0:
        for i in range(0, num_repl):
            shutil.copyfile(last_path, "frame/frame-%d.jpg" % (last_path_number+i+1))