from tkinter import *
from tkinter import ttk, colorchooser

import keras
import cv2
from PIL import ImageTk, Image, ImageDraw
import PIL


class main:
    def __init__(self, master, title, icon):
        self.master = master
        self.master.title(title)
        self.master.iconbitmap(icon)
        self.model = keras.models.load_model("trained_model.h5")
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.counter = 0
        self.draw_widgets()
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def paint(self, e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth,
                               fill=self.color_fg, capstyle=ROUND, smooth=True)
            self.draw.line([self.old_x, self.old_y, e.x, e.y],
                           fill="black", width=8)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):
        self.old_x = None
        self.old_y = None

    def changeW(self, e):
        self.penwidth = e

    def clear(self):
        self.c.delete(ALL)
        self.c2.delete(ALL)
        self.counter = 0
        self.image1 = PIL.Image.new("RGB", (200, 200), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image1)

    def change_fg(self):
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):
        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]

    def save(self):
        filename = "Data/image" + str(self.counter) + ".png"
        self.image1.save(filename)
        self.counter += 1

    def preprocess(self):
        img = cv2.imread("Data/image" + str(self.counter) + ".png")

        img_res = cv2.resize(img, dsize=(
            28, 28), interpolation=cv2.INTER_CUBIC)
        img_res_g = cv2.cvtColor(img_res, cv2.COLOR_BGR2GRAY)
        self.img = img_res_g.reshape(1, 28, 28, 1)

    def classify(self):
        self.preprocess()
        prediction = self.model.predict(self.img)
        result = prediction.argmax()
        self.c2.create_text(20, 30, anchor=W, font="Purisa",
                            text="Predicted digit: "+str(result))
        pass

    def draw_widgets(self):
        width = 500
        height = 400
        self.controls = Frame(self.master, padx=5, pady=5)
        Label(self.controls, text='Penwidth', font=(
            'arial 18')).grid(row=0, column=0)
        self.slider = ttk.Scale(self.controls, from_=100,
                                to=5, command=self.changeW, orient=VERTICAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1, ipadx=30)
        self.controls.pack(side=LEFT)

        self.c = Canvas(self.master, width=200,
                        height=200, bg=self.color_bg,)
        self.image1 = PIL.Image.new("RGB", (200, 200), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image1)
        self.c.pack(fill=BOTH, expand=True)
        self.c2 = Canvas(self.master, width=200,
                         height=50, bg=self.color_bg,)
        self.c2.pack(fill=BOTH, expand=True)

        savebutton = Button(self.controls, text="Save", command=self.save)
        # place(relx=0.55, rely=0.9,relwidth=0.5, relheight=0.3)
        savebutton.grid(row=1, column=0)

        classifyButton = Button(
            self.controls, text="Classify", command=self.classify)
        classifyButton.grid(row=2, column=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='Colors', menu=colormenu)
        colormenu.add_command(label='Brush Color', command=self.change_fg)
        colormenu.add_command(label='Background Color', command=self.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options', menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas', command=self.clear)
        optionmenu.add_command(label='Exit', command=self.master.destroy)


if __name__ == '__main__':
    root = Tk()
    img = "Data/paint.ico"
    title = 'Paint'
    main(root, title, img)
    root.mainloop()
