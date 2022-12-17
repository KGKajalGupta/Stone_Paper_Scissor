
from tkinter import*
                                                                                                # PIL use for images
from random import randint
ubantu = Tk()

ubantu.title("Rock Paper and Scissor")
ubantu.config(bg="black")                  # we config use to editing we can use configure and background or config and bg also

# This is image right and left

rock = PhotoImage(file="SPOILER_rock.png")
paper = PhotoImage(file="SPOILER_paper.png")
scissor = PhotoImage(file="SPOILER_scissor.png")

# Image lable for formatting image 
# Grid is used for position

label_player = Label(ubantu, image=scissor, width=255, height=300)
lable_computer = Label(ubantu, image=scissor, width=255, height=300)
lable_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)


# showing score and indicate the score of player

computer_score = Label(ubantu,text=0, font=("arial", 60, "bold"), bg="light blue", fg="red")
player_score = Label(ubantu,text=0, font=("arial", 60, "bold"), bg="light blue", fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1, column=3)


# This is for indication player and computer tab

player_indicator = Label(ubantu, font=("arial",30,"bold"),text="PLAYER",bg="light blue", fg="red")
computer_indicator = Label(ubantu, font=("arial",30,"bold"),text="COMPUTER",bg="light blue", fg="red")
computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0, column=3)


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
 
#  this is for checkinf the result
    
def winner_check(p,c):
    if p == c:
        msg_updation("it's a tie")
    elif p == "rock":
        if c == "paper":
            msg_updation ("Computer wins")
            computer_update()
        else:
            msg_updation("Player wins")
            player_update()
    elif p == "paper":
        if c == "scissor":
            msg_updation("Computer Wins")
            computer_update()
        else:
            msg_updation("Player wins")
            player_update()
    elif p == 'scissor':
        if c == "rock":
            msg_updation("Computer Wins")
            computer_update()
        else:
            msg_updation("Player Wins")
            player_update
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

final_msg = Label(ubantu, width=15, height=1,font=("arial", 20, "bold",),bg="black", fg="white")
final_msg.grid(row=4,column=2)

# for button making

button_rock = Button(ubantu,width=15, height=3, text="ROCK", font=("arial",20,"bold"),
                      bg="light green",fg="blue", command=lambda:choice_update("rock")).grid(row=2, column = 1)
button_paper = Button(ubantu, width=15, height=3, text="Paper", font=("arial",20,"bold"),
                      bg="light green", fg="red", command=lambda:choice_update("paper")).grid(row=2, column = 2)
button_scissor = Button(ubantu, width = 15, height=3, text="Scissor", font=("arial", 20,"bold"),
                        bg="light green", fg="green", command=lambda:choice_update("scissor")).grid(row=2,column=3)



ubantu.mainloop()