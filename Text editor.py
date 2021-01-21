from pynput.keyboard import Key, Listener, KeyCode, GlobalHotKeys
from os import system
from sys import argv
from tkinter import filedialog, Tk, Text, END
from time import sleep

cmdPressed = False
oPressed = False
WholeString = []
HaveGottenCtrlO = False
CtrlO = ""
TempWholeString = ""

root = Tk("Spann45's text editor")
T = Text(root, width=1920, height=1080)
T.pack()

COMBINATION = {Key.ctrl_l, KeyCode(char='o')}



def openFile(event):
    system('cls')
    global WholeString, fileName, T, TempWholeString
    fileName = filedialog.askopenfilename(initialdir="/", title="Open A File")
    with open(fileName, "rt") as TheFile:
        TempWholeString = TheFile.read()
        for Letter in TempWholeString:
            WholeString.append(Letter)
        
        T.insert(END, ''.join(WholeString))
            

openFile("")

def on_press(key):
    global WholeString, COMBINATION, root
    '''if key in COMBINATION:
        current.add(key)
        if (current.__len__() > 1):
            openFile()'''


    if key == Key.esc:
        quit()

    with open(fileName, "wt") as TheFile:
        if key == Key.space:
            TheLoging = " "

        elif key == Key.enter:
            TheLoging = "\n"
        
        elif key == Key.shift:
            TheLoging = ""

        elif key == Key.backspace:
            TheLoging = ""
            try:
                del WholeString[-1]
            except:
                pass
        
        elif len(key.__str__()) > 3:
            TheLoging = ""

        else:
            TheLoging = ""
            for i in range(0, len(key.__str__())-1):
                if not key.__str__()[i] == "'":
                    TheLoging += key.__str__()[i]
        indexOf = 0
        WholeStringBefore = WholeString
        WholeString += TheLoging
        for i in range(0, len(WholeStringBefore)):
            if WholeStringBefore[i] == "\n":
                indexOf += 1
        
        TempIndex1 = 0
        TempIndex2 = 0
        for i in range(0, len(WholeStringBefore)):
            
            if WholeStringBefore[i] == "\n":
                TempIndex1 += 1
                continue

            if TempIndex1 == indexOf:
                TempIndex2 += 1



        T.insert(END, ''.join(WholeString))
        print(float(str(indexOf) + "." + str(TempIndex2-1)))
        print(''.join(WholeString))
        T.delete(1.0, float(str(indexOf+1) + "." + str(TempIndex2)))
        TheFile.write(''.join(WholeString))
        TheFile.close()


 
def on_release(key):
    global WholeString, COMBINATION
    '''if key in COMBINATION:
        sleep(0.3)
        current.remove(key)
        try:
            T.delete(1.0, END)
        except:
            pass
        T.insert(END, current)'''

listener = Listener(on_press=on_press, on_release=on_release)
listener.start()


def on_activate_o():
    openFile("")

ctrlO = GlobalHotKeys({'<ctrl>+o': on_activate_o})
ctrlO.start()

root.mainloop()