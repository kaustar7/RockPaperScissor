from random import random
import string
from tkinter import *
from PIL import ImageTk, Image


class Icon:
    
    def __init__(self, file, width, height) -> None:
        self.file = file
        self.width = width
        self.height = height
        image = Image.open(self.file)
        resize_image = image.resize((self.width, self.height))
        self.icon = ImageTk.PhotoImage(resize_image)

    def reply(self, result):
        reply_list = ['rock_image.png', 'paper_image.png', 'scissors_image.png']
        file = reply_list[int(3 * random())]
        image = Image.open(file)
        resize_image = image.resize((200,200))
        self.icon = ImageTk.PhotoImage(resize_image)
        mylabel = Button(frame, image = self.icon)
        mylabel.grid(column = 3, row = 2)
        
        if (file == 'paper_image.png' and result == 'scissors_image.png') \
            or (file == 'rock_image.png' and result == 'paper_image.png') \
            or (file == 'scissors_image.png' and result == 'rock_image.png')    :
            Label(frame, text="Winner", width = 10 ).grid(column = 3, row = 3)
        elif file == result:
            Label(frame, text = "Retry", width = 10).grid(column = 3, row = 3)
        else:
            Label(frame, text="Failure", width = 10).grid(column = 3, row = 3)




#start of program
root = Tk() 
root.title("Rock Paper Scissor")


#grid
frame = Frame(root, bg = "cyan")
frame.grid(column = 0, row = 0)


#Rock icon
rock_icon = Icon('rock_image.png', 200, 200)
image1 = rock_icon.icon
rock = Button(frame, image = image1, command = lambda: rock_icon.reply('rock_image.png'))
rock.grid(row = 1 ,column= 2)
#Paper icon
paper_icon = Icon('paper_image.png', 200, 200)
image2 = paper_icon.icon
paper = Button(frame, image = image2, command = lambda: paper_icon.reply('paper_image.png'))
paper.grid(row = 2 ,column= 2)
#Scissor icon
scissor_icon = Icon("scissors_image.png", 200, 200)
image3 = scissor_icon.icon
scissor = Button(frame, image = image3, command = lambda: scissor_icon.reply('scissors_image.png'))
scissor.grid(row = 3 ,column= 2)


root.mainloop()
