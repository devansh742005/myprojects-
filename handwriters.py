import os
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
import subprocess

# Function to generate handwritten image
def generate_handwriting():
    text = entry.get()
    title = entryq.get()

    # Define the output directory
    output_dir = r"C:\Users\ADMIN"
    output_image_path = os.path.join(output_dir, f"{title}.png")

    # Generate the handwritten image
    text_to_handwriting(text, output_image_path)

    # Open the image using the default application
    subprocess.run(['start', output_image_path])

# Function to convert text to handwriting
def text_to_handwriting(text, output_image_path, font_size=30):
    # Load font (Arial)
    font = ImageFont.truetype("arial.ttf", font_size)

    # Split text into lines
    lines = text.split('\n')

    # Create a blank image to calculate text size
    temp_image = Image.new("RGB", (1, 1), color=(255, 255, 255))
    draw = ImageDraw.Draw(temp_image)

    # Calculate the maximum line width and total height
    max_line_width = 0
    total_height = 0
    for line in lines:
        line_width, line_height = draw.textsize(line, font=font)
        max_line_width = max(max_line_width, line_width)
        total_height += line_height

    # Create a blank image with calculated size
    image = Image.new("RGB", (max_line_width, total_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Draw text on the image
    y_offset = 0
    for line in lines:
        width, height = draw.textsize(line, font=font)
        draw.text(((max_line_width - width) / 2, y_offset), line, font=font, fill=(0, 0, 0))
        y_offset += height

    # Save image to file
    image.save(output_image_path)
    print(f"Handwritten image saved to {output_image_path}")

# GUI setup
r = tk.Tk()
r.geometry("500x500")
r.title("Handwritten Text Generator")

label = tk.Label(r, text="Handwritten Text Generator", font=('Papyrus', 18))
label.pack(padx=20, pady=20)

label1 = tk.Label(r, text="Enter Text:", font=('Papyrus', 10))
label1.pack(padx=20, pady=5)

entry = tk.Entry(r, width=40)
entry.pack(padx=40, pady=5)

labelq = tk.Label(r, text="Enter Title:", font=('Papyrus', 10))
labelq.pack(padx=20, pady=5)

entryq = tk.Entry(r, width=40)
entryq.pack(padx=40, pady=5)

button_frame = tk.Frame(r)
button_frame.pack(pady=20)

btn1 = tk.Button(button_frame, text="Generate Handwriting", font=('Papyrus', 12), command=generate_handwriting)
btn1.pack(side=tk.LEFT, padx=10)

btn2 = tk.Button(button_frame, text="Exit", font=('Papyrus', 12), command=r.destroy)
btn2.pack(side=tk.RIGHT, padx=10)

r.mainloop()
