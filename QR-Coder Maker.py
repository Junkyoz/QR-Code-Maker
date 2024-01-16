import qrcode
import os
import tkinter as tk
from PIL import ImageTk, Image


def check_and_display_image(image_path, label):
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img = img.resize((250, 250))
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo
        label.place(x=75, y=170)

def get_content(ent, image_path, label):
    content = ent.get()
    qr = qrcode.make(content)
    qr.save(image_path)
    check_and_display_image(image_path, label)

root = tk.Tk()
root.title('QR-Code Maker')
root.resizable(False, False)
root.geometry('400x500')

head = tk.Label(root, text='Put in URL or Text', font=("Arial", 15))
head.place(x=125,y=30)

ent = tk.Entry(root, width=45)
ent.place(x=65, y=80)

button = tk.Button(root, command=lambda: get_content(ent, 'file.png', label), text='Generate', height=1, width=12)
button.place(x=160, y=110)

image_path = 'file.png'

label = tk.Label(root)
label.pack()

check_and_display_image(image_path, label)

root.mainloop()
