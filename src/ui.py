import tkinter as tk

def start_ui(translate_speech):
    def on_translate():
        original, translated = translate_speech()
        if original and translated:
            original_label.config(text=f"Original: {original}")
            translated_label.config(text=f"Translated: {translated}")

    root = tk.Tk()
    root.title("AI Translator")

    global original_label, translated_label
    original_label = tk.Label(root, text="Original: ")
    original_label.pack()

    translated_label = tk.Label(root, text="Translated: ")
    translated_label.pack()

    translate_button = tk.Button(root, text="Translate", command=on_translate)
    translate_button.pack()

    root.mainloop()
