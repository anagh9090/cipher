import tkinter as tk
from tkinter import scrolledtext
import time

class SecretCoderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SECRET ENCRYPTOR")
        self.root.geometry("500x600")
        self.root.configure(bg="#050505")

        # Codeword Dictionary (Phrases only)
        self.alphabet_code = {
            'A': "Alpha Protocol Active",    'B': "Blueberry Nights",
            'C': "Cipher Detected",         'D': "Dark Matter Rising",
            'E': "Epilepsy Warnings",       'F': "Frequency Jammed",
            'G': "Ghost Protocol",          'H': "Hi, I am a boy",
            'I': "Ionic Charge",            'J': "Jupiter Alignment",
            'K': "Kinetic Energy",          'L': "Love is in the air",
            'M': "Midnight Signal",         'N': "Neon Horizon",
            'O': "Only for you",          'P': "Phantom Pulse",
            'Q': "Quantum State",           'R': "Redacted Entry",
            'S': "Starry Night Sky",        'T': "Time Flies Fast",
            'U': "Underground Network",     'V': "Vector Point",
            'W': "Winter is Coming",        'X': "X-ray Vision",
            'Y': "You are Awesome",       'Z': "Zero Day Alert"
        }

        # --- UI ELEMENTS ---
        tk.Label(root, text="MESSAGE ENCRYPTOR", fg="#00FF00", bg="#050505", 
                 font=("Courier", 14, "bold")).pack(pady=15)

        self.entry = tk.Entry(root, width=40, bg="#111", fg="#00FF00", 
                              insertbackground="#00FF00", font=("Courier", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", lambda e: self.encrypt())

        # Button Frame
        btn_frame = tk.Frame(root, bg="#050505")
        btn_frame.pack(pady=10)

        self.encrypt_btn = tk.Button(btn_frame, text="ENCRYPT", command=self.encrypt,
                                     bg="#00FF00", fg="#000", font=("Courier", 10, "bold"), width=12)
        self.encrypt_btn.grid(row=0, column=0, padx=5)

        self.copy_btn = tk.Button(btn_frame, text="COPY ALL", command=self.copy_to_clipboard,
                                  bg="#333", fg="#00FF00", font=("Courier", 10), width=12)
        self.copy_btn.grid(row=0, column=1, padx=5)

        # Output Area
        self.output_area = scrolledtext.ScrolledText(root, width=50, height=20, 
                                                     bg="#000", fg="#00FF00", 
                                                     font=("Courier", 11), borderwidth=0)
        self.output_area.pack(pady=10, padx=10)

    def encrypt(self):
        self.output_area.delete('1.0', tk.END)
        text = self.entry.get()
        
        for char in text:
            upper_char = char.upper()
            if upper_char in self.alphabet_code:
                line = self.alphabet_code[upper_char] + "\n"
            elif char == " ":
                line = "\n" # Blank line for space
            else:
                line = char + "\n" # Print punctuation/numbers as they are
            
            self.output_area.insert(tk.END, line)
            self.output_area.see(tk.END)
            self.root.update()
            time.sleep(0.03)

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output_area.get('1.0', tk.END).strip())
        self.copy_btn.config(text="COPIED!", fg="white")
        self.root.after(2000, lambda: self.copy_btn.config(text="COPY ALL", fg="#00FF00"))

if __name__ == "__main__":
    root = tk.Tk()
    app = SecretCoderGUI(root)
    root.mainloop()