import cv2
import numpy as np

red = np.uint8([[[255, 0, 0]]])
red_HSV = cv2.cvtColor(red, cv2.COLOR_RGB2HSV)
print(red_HSV)
