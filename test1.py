from guizero import App, Text, TextBox, Slider, PushButton
from gpiozero import LED

# Establishes LEDs
led1 = LED(17)
led2 = LED(4)

window1 = App("Loring's Temperature Control Program", width=370, height=300, layout="grid")


Text(window1, text="", grid=[0, 0])


def fnSliderChange(slider_value):
    numDesTemp1 = float(sldDesTmp.get()) - float(sldDedBnd.get())
    numDesTemp2 = float(sldDesTmp.get()) + float(sldDedBnd.get())
    varRoomTmp = float(sldRoomTmp.get())
    if varRoomTmp < numDesTemp1 :
        txtActSplay.set("Heating")
        print ("Heating")
        led1.on()
        led2.off()
    elif varRoomTmp > numDesTemp2 :
        txtActSplay.set("Cooling")
        print ("Cooling")
        led2.on()
        led1.off()
    else:
        txtActSplay.set("")
        print ("Nothin")
        led1.off()
        led2.off()


Text(window1, text="\nRoom Temperature", grid=[1, 1], align="right")
sldRoomTmp = Slider(window1, start=50, end=120, command=fnSliderChange, grid=[1, 2], align="left")
# Band definition

Text(window1, text="", grid=[2, 1])
Text(window1, text="\nDesired Temperature", grid=[3, 1], align="right")
sldDesTmp = Slider(window1, start=50, end=120, grid=[3, 2], align="left", command=fnSliderChange)

Text(window1, text="", grid=[4, 1])
Text(window1, text="\nDead Band", grid=[5, 1], align="right")
sldDedBnd = Slider(window1, start=-20, end=20, grid=[5, 2], align="left", command=fnSliderChange)
txtSpeed = Text(window1, grid=[0, 0], align="left")

button = PushButton(window1, text="Exit", grid=[8, 2], command=quit)
Text(window1, text="", grid=[6, 1])
txtActionDisp = Text(window1, text="Action:", grid=[7, 1], align="right")

txtActSplay = Text(window1, text="", grid=[7, 2])

sldRoomTmp.set(75)
sldDesTmp.set(75)
sldDedBnd.set(1)

window1.display()

