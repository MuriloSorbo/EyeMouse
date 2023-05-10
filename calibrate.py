import cv2
import winsound
import json
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)

def SaveData(minX, maxX, minY, maxY):
    data = { 
        'minX': minX,
        'maxX': maxX,
        'minY': minY,
        'maxY': maxY,
    }

    with open("calInfo.json", "w") as file:
        json.dump(data, file)

def Run():
    nose = 5
    mouthUp = 13
    mouthDown = 14

    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    i = 0

    command = 'Olhe para a esquerda'
    winsound.Beep(1000, 30)

    while True:
    
        ret, img = cap.read()

        if not ret:
            break
        
        img = cv2.flip(img, 1)
        
        img, faces = detector.findFaceMesh(img, draw=True)

        cv2.putText(img, command, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
        i += 1

        if faces:
            face = faces[0]
            i += 1

            if i / 60 == 3:
                minX = face[nose][0]
                winsound.Beep(1000, 30)
                command = 'Olhe para a direita'

            if i / 60 == 6:
                maxX = face[nose][0]
                winsound.Beep(1000, 30)
                command = 'Olhe para cima'

            if i / 60 == 9:
                minY = face[nose][1]
                winsound.Beep(1000, 30)
                command = 'Olhe para baixo'

            if i / 60 == 12:
                maxY = face[nose][1]
                winsound.Beep(1000, 30)
                SaveData(minX, maxX, minY, maxY)
                break

        cv2.imshow('img', img)
        cv2.waitKey(1)