from tkinter import *
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
pwmRed = GPIO.PWM(23, 500)
pwmRed.start(100)
pwmGreen = GPIO.PWM(18, 500)
pwmGreen.start(100)
pwmBlue = GPIO.PWM(24, 500)
pwmBlue.start(100)


class App:
    def __init__(self, master):
        self.var_R = IntVar()
        self.var_G = IntVar()
        self.var_B = IntVar()
        frame = Frame(master)
        frame.pack()
        Label(frame, text='Red').pack(side=LEFT)
        scaleRed = Scale(frame, variable=self.var_R, from_=0, to=100,
                         orient=HORIZONTAL, command=self.updateRed)
        scaleRed.pack(side=LEFT)
        Label(frame, text='Green').pack(side=LEFT)
        scaleGreen = Scale(frame, variable=self.var_G, from_=0, to=100,
                           orient=HORIZONTAL, command=self.updateGreen)
        scaleGreen.pack(side=LEFT)
        Label(frame, text='Blue').pack(side=LEFT)
        scaleBlue = Scale(frame, variable=self.var_B, from_=0, to=100,
                          orient=HORIZONTAL, command=self.updateBlue)
        scaleBlue.pack(side=LEFT)

    def updateRed(self, duty):  #
        main.configure(background=(self.rgb_to_hex(
            self.var_R, self.var_G, self.var_B)))
        # change the led brightness to match the slider
        pwmRed.ChangeDutyCycle(float(duty))
        pass

    def updateGreen(self, duty):
        main.configure(background=(self.rgb_to_hex(
            self.var_R, self.var_G, self.var_B)))
        pwmGreen.ChangeDutyCycle(float(duty))
        pass

    def updateBlue(self, duty):
        main.configure(background=(self.rgb_to_hex(
            self.var_R, self.var_G, self.var_B)))
        pwmBlue.ChangeDutyCycle(float(duty))
        pass

    def rgb_to_hex(self, r, g, b):
        r = int(r.get() * 255 / 100)
        g = int(g.get() * 255 / 100)
        b = int(b.get() * 255 / 100)
        return '#%02X%02X%02X' % (r, g, b)


main = Tk()  # 8
main.eval('tk::PlaceWindow . center')
main.wm_title('RGB LED Control')
mainFrame = App(main)
main.geometry("500x200")
main.resizable(False, False)
main.configure(background=('#000000'))

try:
    main.mainloop()
finally:
    print("Cleaning up")
    GPIO.cleanup()
