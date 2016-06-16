from tkinter import *
tk = Tk()
canvas =Canvas(tk,width=400,height=400)
canvas.pack()
my_image=PhotoImage(file="ball.gif")
for x in range (1,10):
	canvas.create_image((x*5),(x*5), anchor=NW, image=my_image)

tk.mainloop()