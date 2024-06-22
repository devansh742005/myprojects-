import spacy
import tkinter as tk
from tkinter import scrolledtext
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Regular expressions for Aadhar number and Account number
AADHAR_REGEX = r"\b\d{4}\s\d{4}\s\d{4}\b"
ACCOUNT_REGEX = r"\b\d{9,18}\b"

def process_text(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Check for Aadhar and Account numbers using regex
    aadhar_numbers = re.findall(AADHAR_REGEX, text)
    account_numbers = re.findall(ACCOUNT_REGEX, text)
    
    structured_data = {
        "text": text,
        "entities": entities,
        "aadhar_numbers": aadhar_numbers,
        "account_numbers": account_numbers
    }
    return structured_data

def display_results(results):
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, "Entities:\n")
    for entity in results["entities"]:
        text_area.insert(tk.END, f"{entity[0]} ({entity[1]})\n")
    
    text_area.insert(tk.END, "\nAadhar Numbers:\n")
    for aadhar in results["aadhar_numbers"]:
        text_area.insert(tk.END, f"{aadhar}\n")
    
    text_area.insert(tk.END, "\nAccount Numbers:\n")
    for account in results["account_numbers"]:
        text_area.insert(tk.END, f"{account}\n")

def process_input():
    text = text_input.get("1.0", tk.END)
    results = process_text(text)
    display_results(results)

app = tk.Tk()
app.title("Text Processor AI")
app.geometry("800x600")

frame = tk.Frame(app)
frame.pack(pady=20)

text_label = tk.Label(frame, text="Enter Text:")
text_label.pack()

text_input = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=100, height=10)
text_input.pack(padx=10, pady=10)

process_button = tk.Button(frame, text="Process Text", command=process_input)
process_button.pack(pady=10)

text_area = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=100, height=20)
text_area.pack(padx=10, pady=10)

app.mainloop()
