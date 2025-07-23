from tkinter import *

root=Tk()

input=Entry(root, width=50)
input.grid(row=0,column=0,columnspan=3)

Button7=Button(root, text="" command="")
Button8=Button(root, text="8" command="")
Button9=Button(root, text="9" command="")
Button4=Button(root, text="4" command="")
Button5=Button(root, text="5" command="")
Button6=Button(root, text="6" command="")
Button1=Button(root, text="1" command="")
Button2=Button(root, text="2" command="")
Button3=Button(root, text="3" command="")
Button0=Button(root, text="0" command="")


Button7.grid()

root=mainloop()