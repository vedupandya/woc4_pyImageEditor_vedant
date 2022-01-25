import tkinter
from tkinter import Label, Menu
from PIL import ImageTk, Image
from tkinter import filedialog

root = tkinter.Tk()
root.title("Photo Editor")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = ws - 1200
y = hs - 675
dimensions = "1200x675"+"+"+str(int(x/2))+"+"+str(int(y/2))
root.geometry(dimensions)
root.resizable(0,0)

#root.eval('tk::PlaceWindow . center')
global img_lbl
img_lbl= Label(root,width = 1000, height = 662,bg="#ffffff")
img_lbl.place(x=0, y=0)

''' Note to self: img is an image. img_current is PhotoImage'''

def open_img():
    global img_lbl, file, img1, img, img_cont
    file = filedialog.askopenfilename(title='open')
    img = Image.open(file)
    img1 = ImageTk.PhotoImage(img)
    #img_cont = img_lbl.create_image(0,0,anchor=NW, image = img1)
    img_lbl.configure(image=img1)

def save_img():
    global img, file   
    img = img.save(file)


def saveas_img():
    global img
    filetypes = [('All Files', '*.*'), 
            ('png', '*.png'),
            ('jpg', '*.jpg')]
    savepath = filedialog.asksaveasfile(mode="wb",filetypes = filetypes, defaultextension = ".jpg")
    img = img.save(savepath)



def flip_v():
    global final_img, img_lbl, img, img_current
    img = img.transpose(method=Image.FLIP_TOP_BOTTOM)
    img_current = ImageTk.PhotoImage(img)
    img_lbl.configure(image = img_current)


def flip_h():
    global final_img, img_lbl, img, img_current
    img = img.transpose(method=Image.FLIP_LEFT_RIGHT)
    img_current = ImageTk.PhotoImage(img)
    img_lbl.configure(image = img_current)


def rot_r():
    global img, img_current
    img = img.transpose(Image.ROTATE_270)
    img_current = ImageTk.PhotoImage(img)
    img_lbl.configure(image = img_current)

def rot_l():
    global img, img_current
    img = img.transpose(Image.ROTATE_90)
    img_current = ImageTk.PhotoImage(img)
    img_lbl.configure(image = img_current)



main_menu = Menu(root)
root.config(menu = main_menu)

file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File",menu=file_menu)

open_menu = Menu(file_menu)
file_menu.add_command(label="Open", command = open_img)


save_menu = Menu(file_menu)
file_menu.add_command(label="Save", command = save_img)

saveas_menu = Menu(file_menu)
file_menu.add_command(label="Save As", command = saveas_img)


flip_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Flip",menu=flip_menu)

vertical_menu = Menu(flip_menu)
flip_menu.add_command(label="Vertical", command = flip_v)

horizontal_menu = Menu(flip_menu)
flip_menu.add_command(label="Horizontal", command = flip_h)


rotate_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Rotate",menu=rotate_menu)

right_menu = Menu(rotate_menu)
rotate_menu.add_command(label="Right", command = rot_r)

left_menu = Menu(rotate_menu)
rotate_menu.add_command(label="Left", command = rot_l)

root.mainloop()
