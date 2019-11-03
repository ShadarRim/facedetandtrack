import cv2, time, camera
import numpy as np
from face import Face

class HaarFaceDetector:

    path = None
    cascade = None

    def __init__(self, path):
        self.path = path
        self.cascade = cv2.CascadeClassifier(path)

    def detect(self, grayFrame, scaleFactor = 1.2, minNeighbours = 3, minSize = (30,30), flags = cv2.CASCADE_SCALE_IMAGE):
        return self.cascade.detectMultiScale(grayFrame, scaleFactor, minNeighbours, flags, minSize)

    def change_Cascade(self, path):
        self.cascade = cv2.CascadeClassifier(path)





