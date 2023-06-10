import currentGameFinder as cgf
import imageDownloader as imd
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Free Games this week')
window.geometry("400x200-50+50")
window.iconbitmap('icon\epic_games_black_logo_icon_147139.ico')

labels = []     # holds dynamic game names
names = cgf.currentName
images = []     # holds dynamic game posters
imageURLS = cgf.currentImage

exts = imd.getImages(imageURLS)

pho = []
for p in range(len(imageURLS)):
    pho.append( tk.PhotoImage(file='imageTemp/'+str(p)+exts[p]) )

for i in range(len(cgf.currentName)):
    labels.append(ttk.Label(window, text=names[i]))
    images.append(ttk.Label(window, image=pho[i]))

for l in range(len(labels)):
    labels[l].pack(ipadx=5, ipady=5, fill=tk.BOTH, expand=True)
    images[l].pack(ipadx=5, ipady=5, fill=tk.BOTH, expand=True)
    
window.mainloop()