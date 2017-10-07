from guizero import App, Text, TextBox, Slider, PushButton

        # "speed" holds the value of the slider

window1 = App("Loring's Totally Cool Temperature Control Program",
             width=370, height=300,
             layout="grid")

Text(window1, text="", grid=[0,0])

Text(window1, text="\nRoom Temperature", grid=[1, 1])
sldRoomTmp = Slider(window1, start=50, end=120, grid=[1, 2], align="left")
#Band definition

Text(window1, text="", grid=[2, 1])

Text(window1, text="\nDesired Temperature", grid=[3, 1])
sldDesTmp = Slider(window1, start=50, end=120, grid=[3, 2], align="left")

Text(window1, text="", grid=[4, 1])

Text(window1, text="\nDead Band", grid=[5, 1])
sldDedBnd = Slider(window1, start=0, end=10, grid=[5, 2], align="left")

Text(window1, text="", grid=[5, 1])

txtSpeed = Text(window1, grid=[0,0], align="left")


button = PushButton(window1, text="Exit", grid=[7, 2], command=quit)

txtActionDisp = Text(window1, text="Action", grid=[6,1])

sldRoomTmp.set(75)
sldDesTmp.set(80)
sldDedBnd.set(7)

window1.display()