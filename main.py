from tkinter import Menu, Button, LEFT

from src.controllers.backend import new_game, restart, user_choose, show_help
from src.views.main_view import root, userChoice, color

# ================= Menu ====================
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='New Game', command=lambda: new_game())
file_menu.add_command(label='Restart', command=lambda: restart())
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)
menubar.add_cascade(label='Menu', menu=file_menu)
help_menu = Menu(menubar, tearoff=False)
help_menu.add_command(label='Help', command=lambda: show_help())
menubar.add_cascade(label='Other', menu=help_menu)

scissors = Button(userChoice, text='Scissors', command=lambda: user_choose('scissors'), highlightcolor=color)
scissors.pack(side=LEFT, padx=5, pady=5)
paper = Button(userChoice, text='Paper', command=lambda: user_choose('paper'), highlightcolor=color)
paper.pack(side=LEFT, padx=5, pady=5)
rock = Button(userChoice, text='Rock', command=lambda: user_choose('rock'), highlightcolor=color)
rock.pack(side=LEFT, padx=5, pady=5)

root.configure(menu=menubar)
root.mainloop()
