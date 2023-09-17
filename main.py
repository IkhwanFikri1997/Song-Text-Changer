import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
import csv
import os

window = tk.Tk()
window.title("Song Text Changer")

frame1 = tk.Frame(master=window, bg='red')

SongTree = ttk.Treeview(frame1,columns=("Name", "Artist"),height=45,show='headings')
SongTree.heading('Name', text="Name")
SongTree.heading('Artist', text="Artist")
with open('song-export.csv') as f:
    reader = csv.DictReader(f,delimiter=',')
    for row in reader:
        SongTree.insert('',tk.END,values=(row['title'],row['artist']))


SearchFr = tk.Frame(master=window,bg='blue')

ws_ent = tk.Entry(SearchFr,width=75,font=(('Helvetica'),15,'bold'))
ws_ent.pack(fill=tk.X,side=tk.LEFT)

def Search():
    val = ws_ent.get()
    selections = []
    print(val)

    for line in SongTree.get_children():
        if val in SongTree.item(line)['values']:
            print(SongTree.item(line)['values'])
            selections.append(line)
    print('search completed')
    SongTree.selection_set(selections)

def Reset():
    for item in SongTree.get_children():
        SongTree.delete(item)
    with open('song-export.csv') as f:
        reader = csv.DictReader(f,delimiter=',')
        for row in reader:
            SongTree.insert('',tk.END,values=(row['title'],row['artist']))

ws_btn1 = tk.Button(SearchFr,text = 'Search', command=Search)
ws_btn1.pack(side=tk.RIGHT)
ws_btn2 = tk.Button(SearchFr,text = 'Reset',command=Reset)
ws_btn2.pack(side=tk.RIGHT)
SearchFr.pack(fill=tk.BOTH,side=tk.TOP,expand=True)


SongTree.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame1.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame1,orient=tk.VERTICAL,command=SongTree.yview)
SongTree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

frame2 = tk.Frame(master=window, bg='yellow')

Countist = 0 
Songist = 0

def checkers():
    global Countist, Songist
    if ((var1.get() == 1)&(var2.get() == 0)):
        Countist = 1
        Songist = 0
    elif ((var1.get() == 0)&(var2.get() == 1)):
        Countist = 0
        Songist = 1
    elif ((var1.get() == 1)&(var2.get() == 1)):
        Songist = 1
        Countist = 1
    else:
        Countist = 0 
        Songist = 0

count = 0 
f4 = open("Songlist.txt","w") 
f4.write("Song List :")
f4.close()

def printTitle(): 
    global count
    f1 = open("namefile.txt","w")
    f2 = open("artistfile.txt","w")
    for selected_item in SongTree.selection():
        item = SongTree.item(selected_item)
        record = item['values']
    print(record)
    f1.write(record[1])
    f2.write(record[2])
    f1.close()
    f2.close()
    print(Countist)
    print(Songist)
    if (Countist == 1):
        count = count + 1
        print("I make a counter text")
        f3 = open("counter.txt","w")
        if (count < 10):
            f3.write("0"+ str(count))
        else:
            f3.write(str(count))
        f3.close()
        print(count)
    elif (Songist == 1):
        print("I make a Songlist")
        f4 = open("Songlist.txt","a") 
        f4.write("\n" + str(record[1]))
        f4.close()

checkfr =  tk.Frame(frame2, width=100)
var1 = tk.IntVar()
var2 = tk.IntVar()
C1 = tk.Checkbutton(checkfr,text="Add Counter Text", variable=var1, onvalue=1, offvalue=0, command=checkers) 
C1.pack(side=tk.LEFT)
ToolTip(C1,msg="The Number will be adding itself when the checkbox left on")
C2 = tk.Checkbutton(checkfr,text="Add the song in the Songlist", variable=var2, onvalue=1, offvalue=0 ,command=checkers)
C2.pack(side=tk.RIGHT)
ToolTip(C2,msg="The Song will be adding itself when the checkbox left on")
checkfr.pack(fill=tk.BOTH,side=tk.LEFT,padx=10)
buttonfr =  tk.Frame(frame2, width=100)
B = tk.Button(frame2,text="Change Song Text", height=3, width=30, command=printTitle)
B.pack()
buttonfr.pack(fill=tk.BOTH,side=tk.RIGHT)
frame2.pack(fill=tk.X,side=tk.BOTTOM, expand=True)

window.mainloop()