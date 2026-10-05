import tkinter as tk 
from PIL import Image,ImageTk
from tkinter import  filedialog
from mlforkidsimages import MLforKidsImageProject



key = "3a588e70-8758-11f1-95f5-1d292e01836af4cffb0e-6d13-450b-a705-e2a4b9bee9d3"

myproject = MLforKidsImageProject(key)
myproject.train_model()

w = tk.Tk()


w.geometry("600x300")
w.config(bg="#F1EEDE")
w.iconbitmap("c.ico")
w.title("apple")




im = ImageTk.PhotoImage(Image.open("bg.png").resize((600,300)))

bg = tk.Label(w, image=im)
bg.image = im
bg.place(x=0, y=0)
        

def upload ():
    global im
    image_upload = filedialog.askopenfilename()
    im = ImageTk.PhotoImage(Image.open(image_upload).resize((150,150)))
    label = tk.Label(w,image=im)
    label.place(x=130,y=128)
    demo = myproject.prediction(image_upload)

    label = demo["class_name"]
    confidence = demo["confidence"]

    l1 = tk.Label(text="'%s' with %d%% confidence" % (label, confidence),bg="#F1EEDE")
    l1.place(x=210,y=60,anchor="center")

   


but = tk.Button(text="upload a photo",bg="#F193B0",command=upload)
but.place(x=210,y=100,anchor="center")




w.mainloop()