import random
import tkinter

#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(call):

    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output

    # 1. Create random integer 1-3 to use as computer's play
    comp_call = random.randint(1,3)
    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated
    if comp_call == 1:
        throw = "rock"
    elif comp_call == 2:
        throw = "paper"
    elif comp_call == 3:
        throw = "scissors"
    # 3. Determine the winner based on what the user chose and what the computer chose
    #   Rock beats Scissors
    #   Paper beats Rock
    #   Scissors beats Paper
    if (throw == "rock" and call == "paper") or (throw == "paper" and call == "scissors") or (throw == "scissors" and call == "rock"):
        result = "You won!"
    #   It's a tie if the computer and user chose the same object
    elif throw == call:
        result = "It's a tie!"
    else:
        result = "You lost!"
    # If the user wins, increase win by 1
    if result == "You won!":
        win += 1
    # Use the output label to write what the computer did and what the result was (win, loss, tie)
    output.config(text=f"Computer did: {throw} \n {result}")
    wins.config(text=f"Wins: {win}")

# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

window = tkinter.Tk()

#Variable to count the number of wins the user gets
win = 0


#START CODING HERE

# 1. Create 3 buttons for each option (rock, paper, scissors)
scissors = tkinter.Button(window, text = "Scissors", bg = "#ff9999", padx=10, pady=5, command=pass_s, width=20)
rock = tkinter.Button(window, text = "Rock", bg = "#80ff80", padx=10, pady=5, command=pass_r, width=20)
paper = tkinter.Button(window, text = "Paper", bg = "#3399ff", padx=10, pady=5, command=pass_p, width=20)
# 2. Create 2 labels for the result and the number of wins
output = tkinter.Label(window, width=20, fg = "red", text="What's your call?")
wins = tkinter.Label(window, width = 20, fg="black", text="Wins:0")
# 3. Arrange the buttons and labels using grid
#scissors.grid(row=0, column=0)
scissors.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
#rock.grid(row=0, column=1)
rock.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
#paper.grid(row=0, column=2)
paper.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
#output.grid(row=1, column=0)
output.pack()
#wins.grid(row=1, column=2)
wins.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)
window.mainloop()
