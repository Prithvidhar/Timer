# This is a program that enables a user to set a timer

from tkinter import *
from tkinter import ttk
import time
def startTimer(minutes, seconds):
    totalsec = float((minutes*60) + seconds)
    nowTime = time.time()
    timerEnd = nowTime + totalsec
    # Setting up a progress bar

    while(timerEnd - nowTime != 0):
        nowTime += 1
        time.sleep(1)
        print('.', end=' ')



    else:
        print('complete')



def main():
    root = Tk()
    root.title('Timer')
    root.rowconfigure(0,weight = 1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)

    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight = 1)
    root.columnconfigure(3, weight=1)

    style = ttk.Style()
    style.configure('Header.TLabel', foreground = 'orange', font = ('Ariel, 24, bold'))
    #adding icon to window
    icon = PhotoImage(file = 'timePoot.png')
    root.iconphoto(False, icon)

    frameH = ttk.Frame(root, height = 50, width = 270)
    frameH.grid(row = 0, column = 0, columnspan =2)

    headLabel = ttk.Label(frameH, text = 'Timer', font = ('Arial', '24','bold'), foreground = 'red')
    headLabel.place(anchor = 'nw', x = 175, y = 0)
    #adding input for user

    minLabel = ttk.Label(root,text = 'minutes:')
    minLabel.grid(row = 1, column = 0)

    min = StringVar()
    minSpin = Spinbox(root,from_ = 0, to = 60, textvariable = min).grid(column = 1,row = 1)

    secLabel = ttk.Label(root, text='seconds:').grid(column = 2, row = 1)
    sec = StringVar()
    secSpin = Spinbox(root, from_=0, to=60, textvariable=sec).grid(column = 3, row = 1)

    # adding button to start timer
    startB = ttk.Button(root, text = 'start', command = lambda : startTimer(min.get(), sec.get())).grid(row = 3, column = 0, columnspan = 4)

    root.mainloop()

if __name__ == '__main__':
    main()


