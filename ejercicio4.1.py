import turtle
def dibujar(x):
	t = turtle.Pen()
	angulo=360/x
	for x in range (1,(x+1)):
		t.forward(100)
		t.left(angulo)

dibujar(6)
turtle.getscreen()._root.mainloop()