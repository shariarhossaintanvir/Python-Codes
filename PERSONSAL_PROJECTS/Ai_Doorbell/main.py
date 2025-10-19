import cv2
import face_recognition
import threading
import playsound

def ring_bell():
    print("🔔 Bell should ring now")
    playsound.playsound('doorbell.wav')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(rgb)

    if faces:
        threading.Thread(target=ring_bell, daemon=True).start()

    cv2.imshow("Test", frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
