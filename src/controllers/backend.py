import os
import sys
import tkinter.messagebox
from random import choice
from tkinter import Label, LEFT, TOP,Tk

from src.views.main_view import result, result2, playerPoint, player, myPoint, root, computerChoice


# ================= Functions ====================
def destroy_it():
    for widgets in result.winfo_children():
        widgets.destroy()


def destroy_it2():
    for widgets in result2.winfo_children():
        widgets.destroy()


def show_help():
    tkinter.messagebox.showinfo('Instruction', 'Welcome to Instruction of RPS Game:\n\n'
                                               'New Game: You can open the game in the new windows\n\n'
                                               'Restart: By this option whole scores will be Zero\n\n'
                                               'Exit: Close the game\n\n'
                                               'Game to 2: When game Score is equal on 2, You can continue the game '
                                               'on Score 1\n\n'
                                               'Good Luck')


def restart():
    answer = tkinter.messagebox.askquestion('Restart', 'Do you want to restart the game?', icon='question')
    if answer == 'yes':
        playerPoint.set(0)
        myPoint.set(0)


def new_game():
    answer = tkinter.messagebox.askquestion('New Game', 'Are you sure to play again?', icon='question')
    if answer == 'yes':
        python = sys.executable
        os.execl(python, python, *sys.argv)


def count_plus(name):
    count_v = name.get()
    count_v += 1
    name.set(count_v)


def show_result():
    destroy_it2()
    Label(result2, text='Player: ').pack(side=LEFT)
    Label(result2, textvariable=playerPoint).pack(side=LEFT)
    Label(result2, text='| ').pack(side=LEFT)
    Label(result2, text='Computer: ').pack(side=LEFT)
    Label(result2, textvariable=myPoint).pack(side=LEFT)
    if playerPoint.get() == 2 and myPoint.get() == 2:
        answer = tkinter.messagebox.askquestion('Game to 2',
                                                'Now, We are equal in Score=2\n do you want to continue in 1:1?',
                                                icon='question')
        if answer == 'yes':
            myPoint.set(myPoint.get() - 1)
            playerPoint.set(playerPoint.get() - 1)

    if playerPoint.get() == 3:
        answer = tkinter.messagebox.askquestion('Player WIns',
                                                'You Won! Excellent\nDo you want to play again?',
                                                icon='question')
        if answer == 'yes':
            python = sys.executable
            os.execl(python, python, *sys.argv)
        else:
            root.destroy()
    elif myPoint.get() == 3:
        answer = tkinter.messagebox.askquestion('Computer WIns', 'Remember Me \n Do you want to play again?',
                                                icon='question')
        if answer == 'yes':
            python = sys.executable
            os.execl(python, python, *sys.argv)
        else:
            root.destroy()


def user_choose(name):
    player.set(name)
    computerChoice.set(choice(['rock', 'paper', 'scissors']))
    destroy_it()
    if player.get() == computerChoice.get():
        Label(result, text='Opps, Equal, Next').pack(side=TOP)
        show_result()
    elif player.get() == "rock":
        if computerChoice.get() == "scissors":
            Label(result, text='Good Choice, Next').pack(side=TOP)
            count_plus(playerPoint)
            show_result()
        elif computerChoice.get() == "paper":
            Label(result, text='Bad Choice, Think Then Choose').pack(side=TOP)
            count_plus(myPoint)
            show_result()
    elif player.get() == "scissors":
        if computerChoice.get() == "paper":
            Label(result, text='Good Choice, Next').pack(side=TOP)
            count_plus(playerPoint)
            show_result()
        elif computerChoice.get() == "rock":
            Label(result, text='Bad Choice, Think Then Choose').pack(side=TOP)
            count_plus(myPoint)
            show_result()
    elif player.get() == "paper":
        if computerChoice.get() == "rock":
            Label(result, text='Good Choice, Next').pack(side=TOP)
            count_plus(playerPoint)
            show_result()
        elif computerChoice.get() == "scissors":
            Label(result, text='Bad Choice, Think Then Choose').pack(side=TOP)
            count_plus(myPoint)
            show_result()
