import tkinter as tk
from tkinter import ttk
from engine import PronunciationEngine
from tips import PronunciationTips

class PronunciationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-language Pronunciation Coach")
        self.engine = PronunciationEngine()
        self.tips = PronunciationTips()

       
        self.label = tk.Label(root, text="Enter your sentence:")
        self.label.pack()

        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack(pady=5)

        self.language_label = tk.Label(root, text="Select language:")
        self.language_label.pack()

        self.language_var = tk.StringVar()
        self.language_dropdown = ttk.Combobox(root, textvariable=self.language_var)
        self.language_dropdown['values'] = ('en', 'es', 'fr', 'de')
        self.language_dropdown.current(0)
        self.language_dropdown.pack(pady=5)

        self.speak_button = tk.Button(root, text="Pronounce", command=self.handle_speak)
        self.speak_button.pack(pady=10)

        self.phonetic_output = tk.Label(root, text="", fg="blue")
        self.phonetic_output.pack()

        self.tip_output = tk.Label(root, text="", fg="green", wraplength=400, justify='left')
        self.tip_output.pack(pady=5)

    def handle_speak(self):
        text = self.text_entry.get()
        lang = self.language_var.get()

        self.engine.speak(text, lang)
        phonetic = self.engine.phonetic(text, lang)
        tip = self.tips.get_tip(text, lang)

        self.phonetic_output.config(text=f"Phonetics: {phonetic}")
        self.tip_output.config(text=f"Tip: {tip}")
