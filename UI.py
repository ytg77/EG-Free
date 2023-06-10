# import currentGameFinder as cgf
import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title('Free Games this week')
window.geometry("400x200-50+50")
window.iconbitmap('icon\epic_games_black_logo_icon_147139.ico')

ls = []
for i in range(5):
    ls.append(ttk.Label(window, text=i))

for w in ls:
    w.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True)

window.mainloop()