import numpy as np
import glob
import cv2
from uploads.core.models import MyImage


def Deneme(filename):
    original = cv2.imread("media/"+filename)
    all_images = glob.iglob("media/images/*")
    all_images_to_compare = []
    titles = []

    result_list = []
    result_titles = []
    i = 1
    for f in glob.iglob("media/images/*"):
        image = cv2.imread(f)
        titles.append(f.title())
        all_images_to_compare.append(image)

    for image_to_compare, title in zip(all_images_to_compare, titles):
        
        i = i + 1
        result_titles.append(title)
        # 1) Check if 2 images are equals

        sift = cv2.xfeatures2d.SIFT_create()
        kp_1, desc_1 = sift.detectAndCompute(original, None)
        kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)
        
        index_params = dict(algorithm=0, trees=5)
        search_params = dict()
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(desc_1, desc_2, k=2)

        good_points = []
        for m, n in matches:
            if m.distance < 0.6 * n.distance:
                good_points.append(m)

        # Define how similar they are
        number_keypoints = 0
        if len(kp_1) <= len(kp_2):
            number_keypoints = len(kp_1)
        else:
            number_keypoints = len(kp_2)

        k = len(good_points) / number_keypoints * 100
        # print("Similarity : %",k)
        # print("\n")

        result_list.append(k)
        print(title)
        print("ok")
    # print(result_list)
    for i in range(len(result_list)):
        for j in range(len(result_list) - 1):
            if float(result_list[j]) < float(result_list[j + 1]):
                temp = result_list[j]
                result_list[j] = result_list[j + 1]
                result_list[j + 1] = temp
                temp = result_titles[j]
                result_titles[j] = result_titles[j + 1]
                result_titles[j + 1] = temp

    # print(result_list)
    # print(result_titles)
    images = []

    if result_list:
        for i in range(6):
            myimage = MyImage()
            paths = result_titles[i].split('/')
            names = paths[2].split('.')
            myimage.name = names[0] + "." + names[1].lower()
            myimage.path = paths[0].lower() + "/" + paths[1].lower() + "/" + myimage.name
            myimage.value = result_list[i]
            images.append(myimage)

    return images