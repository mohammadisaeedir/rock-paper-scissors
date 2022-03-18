from tkinter import StringVar, IntVar, Frame, Tk, TOP, Label, BOTTOM, LEFT

# ================= Settings ====================
root = Tk()
root.title('Rock, Paper, Scissors')
root.geometry('300x140')
root.resizable(width=False, height=False)
color = 'purple'
player = StringVar(value='------')
computerChoice = StringVar(value='------')
playerPoint = IntVar()
myPoint = IntVar()

# ================= Frames ====================
userChoice = Frame(root, width=300, height=50)
userChoice.pack(side=TOP)
computer = Frame(root, width=300, height=50, bg=color)
computer.pack(side=TOP)
result = Frame(root, width=300, height=50)
result.pack(side=TOP)
result2 = Frame(root, width=300, height=50)
result2.pack(side=TOP)
footer = Frame(root, width=300, height=10)
footer.pack(side=BOTTOM)

# ================= Labels and Buttons ====================
topLabel = Label(userChoice, text='Choose: ')
topLabel.pack(side=LEFT, padx=5, pady=5)
user_label = Label(computer, text='User Choice: ')
user_label.pack(side=LEFT, padx=5, pady=5)
playerPick = Label(computer, textvariable=player)
playerPick.pack(side=LEFT, padx=5, pady=5)
computerLabel = Label(computer, text='Computer: ')
computerLabel.pack(side=LEFT, padx=5, pady=5)
computerPick = Label(computer, textvariable=computerChoice)
computerPick.pack(side=LEFT, padx=5, pady=5)
sign = Label(footer, text='Developed By Saeed')
sign.pack(side=TOP)
