# -*- coding:utf-8 -*-
import cv2

img = cv2.imread('./Lenna.jpg', cv2.IMREAD_GRAYSCALE)

detector = cv2.FeatureDetector_create('FAST')
keypoints = detector.detect(img)

out_img = cv2.drawKeypoints(img, keypoints, 0)

cv2.imshow('imshow_test', out_img)
cv2.waitKey(0)
