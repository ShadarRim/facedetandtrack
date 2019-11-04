import cv2, time, camera
import numpy as np
from face import Face
from face_detector import HaarFaceDetector
from face_tracker import TemplateTracking
import util

debug_Time = True
debug_Tracking_Results = False
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

    if debug_Time:
        curTime = time.time()
        faceToTrack = len(faces)

    if faces:
        index = 0
        while index < len(faces):
            face = faces[index]
            min, max, minLoc, maxLoc = tracker.do_Track_in_Frame(face.mat, face.pos, grayFrame)
            if debug_Tracking_Results:
                print(f'ID {face.id} Min {min}  Max {max}')
            if min > 0.05:
                del faces[index]
            else:
                cv2.rectangle(frame, minLoc, (minLoc[0] + face.cows(), minLoc[1] + face.rows()), (0, 255, 255), 2)
                index += 1

    if debug_Time:
        print(f'We spent {round((time.time()-curTime)*1000,2)} ms to track {faceToTrack} objects on one frame')
        curTime = time.time()

    faces_from_det = detector.detect(grayFrame)

    for (x, y, w, h) in faces_from_det:
        is_new = True
        if faces:
            for face in faces:
                iuu = util.iuu(x, y, w, h, face.pos[0], face.pos[1], face.pos[2], face.pos[3])
                if iuu > 0.2:
                    is_new = False

        if is_new:
            faces.append(Face(grayFrame[y:y+h, x:x+w], (x, y, w, h), id))
            id += 1

    if debug_Time:
        print(f'We sepnt {round((time.time()-curTime)*1000,2)} ms to detect faces on one frame')


    frame = cv2.flip(frame, 1)
    cv2.imshow('Webcam test frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

