from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Button
ActivePlayer=1
P1=[]
P2=[]

root=Tk()
root.title('TIC TAC TOE GAME. Player 1:')
style=ttk.Style()
style.theme_use('classic')
#add buttons
Bu1=ttk.Button(root,text=' ')
Bu1.grid(column=0,row=0,sticky='snew',ipadx=40,ipady=40)

Bu1.config(command=lambda:BuClick(1))


Bu2=ttk.Button(root,text=' ')
Bu2.grid(column=1,row=0,sticky='snew',ipadx=40,ipady=40)
Bu2.config(command=lambda:BuClick(2))
Bu3=ttk.Button(root,text=' ')
Bu3.grid(column=2,row=0,sticky='snew',ipadx=40,ipady=40)
Bu3.config(command=lambda:BuClick(3))
Bu4=ttk.Button(root,text=' ')
Bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
Bu4.config(command=lambda:BuClick(4))

Bu5=ttk.Button(root,text=' ')
Bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
Bu5.config(command=lambda:BuClick(5))

Bu6=ttk.Button(root,text=' ')
Bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
Bu6.config(command=lambda:BuClick(6))

Bu7=ttk.Button(root,text=' ')
Bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
Bu7.config(command=lambda:BuClick(7))

Bu8=ttk.Button(root,text=' ')
Bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
Bu8.config(command=lambda:BuClick(8))

Bu9=ttk.Button(root,text=' ')
Bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
Bu9.config(command=lambda:BuClick(9))


def BuClick(id):
    global ActivePlayer
    global P1
    global P2
    if (ActivePlayer == 1):
            setlayout(id, 'X')
            P1.append(id)
            root.title('TIC TAC TOE GAME. Player 2:')
            ActivePlayer = 2
            print("P1:{}".format(P1))


    elif(ActivePlayer ==2):
        setlayout(id, 'O')
        P2.append(id)
        root.title('TIC TAC TOE GAME. Player 1:')
        ActivePlayer = 1
        print("P2:{}".format(P2))

    CheckWinner()

def CheckWinner():
    winner=-1
    if((1 in P1)and (2 in P1) and (3 in P1) ):
        winner=1
    if ((1 in P2) and (2 in P2) and (3 in P2)):
        winner = 2
    if((4 in P1)and (5 in P1) and (6 in P1) ):
        winner=1
    if ((4 in P2) and (5 in P2) and (6 in P2)):
        winner = 2
    if((7 in P1) and (8 in P1) and (9 in P1)):
        winner=1
    if ((7 in P2) and (8 in P2) and (9 in P2)):
        winner = 2
    if ((1 in P1) and (4 in P1) and (7 in P1)):
        winner=1
    if ((1 in P2) and (4 in P2) and (7 in P2)):
        winner=2
    if ((2 in P1) and (5 in P1) and (8 in P1)):
        winner=1
    if ((2 in P2) and (5 in P2) and (8 in P2)):
        winner=2
    if ((3 in P1) and (6 in P1) and (9 in P1)):
        winner=1
    if ((3 in P2) and (6 in P2) and (9 in P2)):
        winner=2
    if ((1in P1) and (5 in P1) and (9 in P1)):
        winner=1
    if ((1in P2) and (5 in P2) and (9 in P2)):
        winner=2
    if ((3 in P1) and (5 in P1) and (7 in P1)):
        winner=1
    if ((3 in P2) and (5 in P2) and (7 in P2)):
        winner=2

    if winner==1:
        messagebox.showinfo(title='CONGRATULATION',message='player 1 is the winner')

    elif winner==2:
        messagebox.showinfo(title='CONGRATULATION',message='player 2 is the winner')

def setlayout(id, playersymbol):
    if (id == 1):
        Bu1.config(text=playersymbol)
        Bu1.state(['disabled'])
    elif (id == 2):
        Bu2.config(text=playersymbol)
        Bu2.state(['disabled'])
    elif (id == 3):
        Bu3.config(text=playersymbol)
        Bu3.state(['disabled'])
    elif (id == 4):
        Bu4.config(text=playersymbol)
        Bu4.state(['disabled'])
    elif (id == 5):
        Bu5.config(text=playersymbol)
        Bu5.state(['disabled'])
    elif (id == 6):
        Bu6.config(text=playersymbol)
        Bu6.state(['disabled'])
    elif (id == 7):
        Bu7.config(text=playersymbol)
        Bu7.state(['disabled'])
    elif (id == 8):
        Bu8.config(text=playersymbol)
        Bu8.state(['disabled'])
    elif (id == 9):
        Bu9.config(text=playersymbol)
        Bu9.state(['disabled'])

root.mainloop()