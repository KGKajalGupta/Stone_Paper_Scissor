
# from tkinter import*

# ubantu = Tk( )

# # tp rename the title of the window
 
# ubantu.title("Kajal Gupta's Game")

# # pack is used to show the object in the window
# # You can set the label so you can make it bigger and smaller

# label = Label(ubantu, text="Stone_Paper_scissor", font=("Arial Bold",50),bg="sky blue", fg= "red").pack()
# ubantu.geometry("850x200")

# # create a button
# but = Button(ubantu,text="Enter yor choice: ",bg="pink", fg="green" ,font=("Arial bold underline", 30)).pack()
# # def clicked():
# #     configure(text="Button was clicked!!")
# # clicked

# ubantu.mainloop()

num = int(input("How many times do you want to play: "))
from tkinter import*
                                                                                                # PIL use for images
from random import randint
ubantu = Tk()

ubantu.title("Rock Paper and Scissor")
ubantu.config(bg="white")                  # we use config to editing we can use configure and background or config and bg also

# This is image right and left

rock = PhotoImage(file="SPOILER_rock.png")
paper = PhotoImage(file="SPOILER_paper.png")
scissor = PhotoImage(file="SPOILER_scissor.png")

# Image lable for formatting image 
# Grid is used for position

label_player = Label(ubantu, image=scissor, width=255, height=350)
lable_computer = Label(ubantu, image=scissor, width=255, height=350)
lable_computer.grid(row=2, column=0)
label_player.grid(row=2, column=4)


# showing score and indicate the score of player

computer_score = Label(ubantu,text=0, font=("arial", 60, "bold"), bg="light blue", fg="red")
player_score = Label(ubantu,text=0, font=("arial", 60, "bold"), bg="light blue", fg="red")
computer_score.grid(row=2,column=1)
player_score.grid(row=2, column=3)


# This is for indication player and computer tab

player_indicator = Label(ubantu, font=("arial",30,"bold"),text="PLAYER",bg="light blue", fg="red")
computer_indicator = Label(ubantu, font=("arial",30,"bold"),text="COMPUTER",bg="light blue", fg="red")
computer_indicator.grid(row=1,column=1)
player_indicator.grid(row=1, column=3)


def msg_updation(a):
    final_msg['text'] = a
    
def computer_update():
    final = int(computer_score['text'])
    final += 1
    computer_score['text']=str(final)

def player_update():
    final = int(player_score['text'])
    final += 1
    player_score['text'] = str(final)

def exit_update():
    ubantu.destroy()

 
#  this is for checkinf the result

count  = 0    
def winner_check(p,c):
    global count
    if count == num-1:
        # msg_updation("Game Over")
        Label(ubantu, width=15, height=1, text="Game Over", font=("arial", 20, "bold",),bg="red", fg="black").grid(row=5,column=2)
        button_exit = Button(ubantu, width = 10, height=1, text="Exit", font=("arial", 20,"bold"),
                        bg="white", fg="green", command=lambda:exit_update()).grid(row=6,column=2)
    elif p == c:
        count += 1
        msg_updation("it's a tie")
    elif p == "rock":
        count += 1
        if c == "paper":
            msg_updation ("Computer wins")
            computer_update()
        else:
            msg_updation("Player wins")
            player_update()
    elif p == "paper":
        count += 1
        if c == "scissor":
            msg_updation("Computer Wins")
            computer_update()
        else:
            msg_updation("Player wins")
            player_update()
    elif p == 'scissor':
        count += 1
        if c == "rock":
            msg_updation("Computer Wins")
            computer_update()
        else:
            msg_updation("Player Wins")
            player_update()
    else:
        pass
    
    
to_select = ["rock", "paper", "scissor"]

# this is for update the photo

def choice_update(a):
    choice_computer = to_select[randint(0,2)]   # it chose randomly from 0 to 2
    if choice_computer == "rock":
        lable_computer.configure(image=rock)
    elif choice_computer == "paper":
        lable_computer.configure(image=paper)
    else:
        lable_computer.configure(image=scissor)
        
    if a == "rock":
        label_player.configure(image=rock)
    elif a == "paper":
        label_player.configure(image=paper)
    else:
        label_player.configure(image=scissor)
        
            
    winner_check(a, choice_computer)


# for final massage

final_msg = Label(ubantu, width=15, height=1,font=("arial", 20, "bold",),bg="white", fg="black")
final_msg.grid(row=4,column=2)

# for button making

button_rock = Button(ubantu,width=15, height=3, text="ROCK", font=("arial",20,"bold"),
                      bg="light green",fg="blue", command=lambda:choice_update("rock")).grid(row=3, column = 1)
button_paper = Button(ubantu, width=15, height=3, text="Paper", font=("arial",20,"bold"),
                      bg="light green", fg="red", command=lambda:choice_update("paper")).grid(row=3, column = 2)
button_scissor = Button(ubantu, width = 15, height=3, text="Scissor", font=("arial", 20,"bold"),
                        bg="light green", fg="green", command=lambda:choice_update("scissor")).grid(row=3,column=3)



ubantu.mainloop()