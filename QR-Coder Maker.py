import qrcode
import sys
import os
import tkinter as tk
from PIL import ImageTk, Image

def app():
    root = tk.Tk()
    root.title('QR-Code Maker')
    root.resizable(False, False)
    root.geometry('400x600')
    
    img = ImageTk.PhotoImage()
    qr_displayed = tk.Label(image=img)
    qr_displayed.pack()
    
    ent = tk.Entry(root)
    ent.pack()
        
    root.mainloop()
    
app()