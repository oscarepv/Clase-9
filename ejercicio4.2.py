import turtle
t = turtle.Pen()
def dibujar(x):
	for x in range (1,(x+1)):
		t.forward(100)
		t.left(144)

dibujar(5) 
turtle.getscreen()._root.mainloop()