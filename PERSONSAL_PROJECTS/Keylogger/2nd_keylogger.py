from pynput.keyboard import Listener
import time
def on_press(key):
	key_str = str(key).replace("'", "")
	if key_str == "Key.space":
		key_str = " "
	print(f"[{time.ctime()}] {key_str}")
# black screen par direct dikhayega
with Listener(on_press=on_press) as listener:
	listener.join()