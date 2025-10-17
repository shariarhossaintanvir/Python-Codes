import cv2
import face_recognition
cap = cv2.VideoCapture(0)
sound_played = False 
while True:
    _ , frame =cap.read()
    faces = face_recognition.face_location(frame)
    print(faces)
    if faces:
        print('Ding Dong')
        sound_played = True
    elif not faces and sound_played:
        sound_playe = False
    cv2.imshow('Smart Doorbell',frame)
    if cv2.waitKey(10) == ord('q'):
        break