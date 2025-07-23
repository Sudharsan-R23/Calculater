from tkinter import *

root=Tk()

input=Entry(root, width=50)
input.grid(row=0,column=0,columnspan=3)

Button7=Button(root, text="7", padx=50, pady=50)
Button8=Button(root, text="8", padx=50, pady=50)
Button9=Button(root, text="9", padx=50, pady=50)
Button4=Button(root, text="4", padx=50, pady=50)
Button5=Button(root, text="5", padx=50, pady=50)
Button6=Button(root, text="6", padx=50, pady=50)
Button1=Button(root, text="1", padx=50, pady=50)
Button2=Button(root, text="2", padx=50, pady=50)
Button3=Button(root, text="3", padx=50, pady=50)
Button0=Button(root, text="0", padx=50, pady=50)


Button7.grid(row=1,column=0)
Button8.grid(row=1,column=1)
Button9.grid(row=1,column=2)
Button4.grid(row=2,column=0)
Button5.grid(row=2,column=1)
Button6.grid(row=2,column=2)
Button1.grid(row=3,column=0)
Button2.grid(row=3,column=1)
Button3.grid(row=3,column=2)
Button0.grid()

root=mainloop()