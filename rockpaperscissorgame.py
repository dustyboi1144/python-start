import tkinter as tk
import random
choices = ["rock", "paper", "scissor"]
def play(handsign):
    computer= random.choice(choices)

    if handsign==computer:
        result="draw!"
    elif((handsign=="rock" and computer=="scissor") 
         or (handsign=="paper" and computer=="rock")
           or (handsign=="scissor" and computer=="paper")):
        result="you win!"
    else:
        result="you lose!"

    computer_label.config(text="computer chose: "+computer)
    result_label.config(text=result)

window=tk.Tk()
window.title("rock paper scissor!")
window.geometry("500x500")
tk.Label(window,text="Choose your handsign!").pack(pady=10)
tk.Button(window,text="rock",font=("Arial",20),width=10,height=2,command=lambda: play("rock")).pack()
tk.Button(window,text="paper",font=("Arial",20),width=10,height=2,command=lambda: play("paper")).pack()
tk.Button(window,text="scissor",font=("Arial",20),width=10,height=2,command=lambda : play("scissor")).pack()

computer_label= tk.Label(text="")
computer_label.pack(pady=10)

result_label= tk.Label(window, text="", font=("Arial",20))
result_label.pack()

window.mainloop()


