
from tkinter import*

ubantu = Tk( )

# tp rename the title of the window
 
ubantu.title("Kajal Gupta's Game")

# pack is used to show the object in the window
# You can set the label so you can make it bigger and smaller

label = Label(ubantu, text="Stone_Paper_scissor", font=("Arial Bold",50),bg="sky blue", fg= "red").pack()
ubantu.geometry("850x200")

# create a button
but = Button(ubantu,text="Enter yor choice: ",bg="pink", fg="green" ,font=("Arial bold underline", 30)).pack()
# def clicked():
#     configure(text="Button was clicked!!")
# clicked

ubantu.mainloop()