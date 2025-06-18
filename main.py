import tkinter as tk
from tkinter import messagebox

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.',
    ')': '-.--.-', ' ': '/'
}

# Encode function
def encode(text):
    encoded = ''
    for char in text.upper():
        encoded += MORSE_CODE_DICT.get(char, '?') + ' '
    return encoded.strip()

# Decode function
def decode(morse):
    reversed_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    decoded = ''
    words = morse.strip().split(' / ')
    for word in words:
        for symbol in word.split():
            decoded += reversed_dict.get(symbol, '?')
        decoded += ' '
    return decoded.strip()

# Button handlers
def handle_encode():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some text to encode.")
        return
    result = encode(text)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

def handle_decode():
    morse = input_text.get("1.0", tk.END).strip()
    if not morse:
        messagebox.showwarning("Input Error", "Please enter Morse code to decode.")
        return
    result = decode(morse)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# GUI setup
window = tk.Tk()
window.title("Morse Code Encoder & Decoder")
window.geometry("600x400")

# Input label and text box
tk.Label(window, text="Input (Text or Morse Code):").pack()
input_text = tk.Text(window, height=5, width=70)
input_text.pack()

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Encode to Morse", command=handle_encode, width=20).pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="Decode to Text", command=handle_decode, width=20).pack(side=tk.LEFT, padx=10)

# Output label and text box
tk.Label(window, text="Output:").pack()
output_text = tk.Text(window, height=5, width=70)
output_text.pack()

# Run the GUI
window.mainloop()
