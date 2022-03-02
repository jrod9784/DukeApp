from cProfile import label
from tkinter import *
from PIL import ImageTk, Image

root = Tk()

canvas = Canvas(root, height = 300, width = 300).pack
title = root.title("Duke Blue Planet")
root.iconbitmap('American_flag.ico')
root.configure(background = "blue")
sweatshirt = Button(root, text = "Blue Duke Sweatshirt, Nike", fg = "blue", padx = 40)
sweatpants = Button(root, text = "Black Duke Sweatpants, Nike", fg = "blue", padx = 34)
quit_button = Button(root, text = "Quit", command = root.quit, fg = "blue")
my_img = ImageTk.PhotoImage(Image.open("DukeSweatpants.png"))
my_label = Button(image = my_img)
my_label.grid(row = 1, column = 2)

my_img2 = ImageTk.PhotoImage(Image.open("DukeSweatshirt.png"))
my_label2 = Button(image = my_img2)
my_label2.grid(row = 1, column = 3)


sweatshirt.grid(row = 0, column = 3)
sweatpants.grid(row = 0, column = 2)
quit_button.grid(row = 20, column = 20,sticky = "se")







root.mainloop()
        
