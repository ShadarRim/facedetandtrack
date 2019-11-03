import cv2, time, camera
import numpy as np
from face import Face
from face_detector import HaarFaceDetector
from face_tracker import TemplateTracking

webcam = camera.default_webcamera(1280, 960)
detector = HaarFaceDetector("haarcascade_frontalface_default.xml")
tracker = TemplateTracking()
faces = []
id = 0

need = True

while True:
    ret, frame = webcam.read()
    if not ret:
        break

    grayFrame = frame[:, :]
    cv2.cvtColor(grayFrame, cv2.COLOR_BGR2GRAY)

    if faces:
        for face in faces:
            min, max, minLoc, maxLoc = tracker.do_Track_in_Frame(face.mat, grayFrame)
            print(f'ID {face.id}Min {min}  Max {max}')
            cv2.rectangle(frame, minLoc, (minLoc[0] + face.cows(), minLoc[1] + face.rows()), (0, 255, 255), 2)

    if need:
        faces_from_det = detector.detect(grayFrame)

        for (x, y, w, h) in faces_from_det:
            faces.append(Face(frame[y:y+h, x:x+w], (x, y, w, h), id))
            id += 1

        need = False

    frame = cv2.flip(frame, 1)
    cv2.imshow('Webcam test frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

