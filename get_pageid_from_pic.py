import cv2
import os
import pytesseract
import numpy as np


pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"

target_dir=r"D:\AllDowns\newbooks\page_mid_pic"

def cv_imread(filePath):
    cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
    return cv_img

for each in os.listdir(target_dir):
    if each.endswith(".png"):

        # https://www.coder.work/article/2087741

        image_path=f"{target_dir}{os.sep}{each}"

        # https://blog.csdn.net/liuqinshouss/article/details/78696032
        # 我就要用中文路径，怎地?

        image=cv_imread(image_path)
        # cv2.namedWindow("lena",cv2.WINDOW_AUTOSIZE)
        # cv2.imshow("lena",img)
        #
        # k=cv2.waitKey(0)
        #
        # cv2.imencode('.jpg', img)[1].tofile('百合.jpg')


        # image = cv2.imread(image_path)
        original = image.copy()
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        except Exception:
            gray = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        gray = 255 - gray

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        dilate = cv2.dilate(gray, kernel, iterations=4)

        cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        image_number = 0
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            ROI = original[y:y + h, x:x + w]
            data = pytesseract.image_to_string(ROI, lang='eng', config='--psm 10')
            if data.isdigit():
                print('Page #: ', data)
                cv2.imwrite("ROI_{}.png".format(image_number), ROI)
                image_number += 1

        cv2.imshow('gray', gray)
        cv2.imshow('dilate', dilate)
        cv2.imshow('original', original)
        cv2.waitKey()

        break