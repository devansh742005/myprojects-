
import tkinter as tk
import qrcode 
import os 

def QR():
 qr_details = entry.get()
 qr_title =  entryq.get()
 img = qrcode.make(qr_details)
 img.save(qr_title + ".png")
 os.system("start {}.png".format(qr_title)) 
 
 
r = tk.Tk()
r.geometry("500x500")
r.title("QR box")
label = tk.Label(r, text="Chatbox", font=('Papyrus', 18))
label.pack(padx=20, pady=20)

label1 = tk.Label(r, text="place ur URl down", font=('Papyrus', 10))
label1.pack(padx=20, pady=20)

entry = tk.Entry(r, width=40)
entry.pack(padx=40, pady=40)


entryq = tk.Entry(r, width=40)
entryq.pack(padx=40, pady=40)

button_frame = tk.Frame(r)
button_frame.pack(pady=20)

btn1 = tk.Button(button_frame, text="1", font=('Papyrus', 18), command=QR)
btn1.grid(row=0, column=0)

r.mainloop()