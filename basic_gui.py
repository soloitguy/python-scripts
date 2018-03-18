from Tkinter import *
import Tkinter
import tkMessageBox



top = Tk()
top.title("What would you like to do today?")

def openAtom():
    file_to_open = "/Applications/Atom.app"
    import subprocess
    subprocess.call(["open", "-a", file_to_open])
def openCode():
    file_to_open = "/Applications/Visual Studio Code.app"
    import subprocess
    subprocess.call(["open", "-a", file_to_open])
def openSpotify():
    file_to_open = "/Applications/Spotify.app"
    import subprocess
    subprocess.call(["open", "-a", file_to_open])
def openChrome():
    file_to_open = "/Applications/Google Chrome.app"
    import subprocess
    subprocess.call(["open", "-a", file_to_open])
def openTerm():
    file_to_open = "/Applications/iTerm.app"
    import subprocess
    subprocess.call(["open", "-a", file_to_open])


w = 800 # width for the Tk root
h = 250 # height for the Tk root

# get screen width and height
ws = top.winfo_screenwidth() # width of the screen
hs = top.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is place
top.geometry('%dx%d+%d+%d' % (w, h, x, y)) 

background_image = PhotoImage(file="/Users/kevin.sullivan/Desktop/mountain.gif") #Load the image for the background
bg_label = Label (top, image=background_image) #Initialize the label 
bg_label.image = background_image # Set a reference
bg_label.grid(ipady=50)


codeButton = Tkinter.Button(bg_label, text ="Write Code in VSC", width=20, pady=10, highlightbackground="black", anchor=W, command = openCode)
atomButton = Tkinter.Button(bg_label, text ="Write Code in Atom", width=20, pady=10, highlightbackground="black", command = openAtom)
spotifyButton = Tkinter.Button(bg_label, text ="Listen to Music", width=20, pady=10, highlightbackground="black", command = openSpotify)
chromeButton = Tkinter.Button(bg_label, text ="Browse the Internet", width=20, pady=10, highlightbackground="black", command = openChrome)
termButton = Tkinter.Button(bg_label, text ="Open the Terminal", width=20, pady=10, highlightbackground="black", command = openTerm)


codeButton.pack()
atomButton.pack()
spotifyButton.pack()
chromeButton.pack()
termButton.pack()
bg_label.pack_propagate(0)
bg_label.pack(fill=BOTH)

top.mainloop()


