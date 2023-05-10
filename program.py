import pyautogui
import cv2
import json
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

def getData():
    with open("calInfo.json", "r") as file:
        return json.load(file)

def calculateToScreen(point, minX, maxX, minY, maxY):
    width = 1366
    height = 768

    return (width / (maxX - minX)) * (point[0] - minX), (height / (maxY - minY)) * (point[1] - minY)

def clicked(mouthUp, mouthDown):
    return abs(mouthUp[1] - mouthDown[1]) > 5

def Run():
    data = getData()

    nose = 5
    mouthUp = 13
    mouthDown = 14

    lastX = 0
    lastY = 0

    while True:
    
        ret, img = cap.read()

        if not ret:
            break
        
        img = cv2.flip(img, 1)
        
        img, faces = detector.findFaceMesh(img, draw=False)

        if faces:
            face = faces[0]

            x, y = calculateToScreen(face[nose], data['minX'], data['maxX'], data['minY'], data['maxY'])
            click = clicked(face[mouthUp], face[mouthDown])

            if (abs(lastX - x) > 10 or abs(lastY - y) > 10):
                pyautogui.moveTo(x, y, _pause=False)

                lastX = x
                lastY = y

            if click:
                pyautogui.leftClick()

        # cv2.imshow('img', img)
        # cv2.waitKey(1)