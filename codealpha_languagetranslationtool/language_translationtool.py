import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Dictionary of languages
languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Russian": "ru"
}

# Translate function
def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter some text.")
        return

    source = languages[source_lang.get()]
    target = languages[target_lang.get()]

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Copy translated text
def copy_text():
    root.clipboard_clear()
    root.clipboard_append(output_text.get("1.0", tk.END))
    messagebox.showinfo("Copied", "Translated text copied!")

# GUI Window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x600")
root.configure(bg="#f2f2f2")

title = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2"
)
title.pack(pady=10)

tk.Label(root, text="Enter Text:", bg="#f2f2f2").pack()

input_text = tk.Text(root, height=8, width=70)
input_text.pack(pady=5)

frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

source_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
source_lang.current(0)
source_lang.grid(row=0, column=0, padx=10)

target_lang = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly",
    width=20
)
target_lang.current(1)
target_lang.grid(row=0, column=1, padx=10)

translate_btn = tk.Button(
    root,
    text="Translate",
    command=translate_text,
    bg="green",
    fg="white",
    font=("Arial", 12, "bold")
)
translate_btn.pack(pady=10)

tk.Label(root, text="Translated Text:", bg="#f2f2f2").pack()

output_text = tk.Text(root, height=8, width=70)
output_text.pack(pady=5)

copy_btn = tk.Button(
    root,
    text="Copy",
    command=copy_text,
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold")
)
copy_btn.pack(pady=10)

root.mainloop()
