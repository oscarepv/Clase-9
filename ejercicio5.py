import turtle
t = turtle.Pen()
def micuadrado(size):
	for x in range (1,5):
		t.forward(size)
		t.left(90)
micuadrado(150)
turtle.getscreen()._root.mainloop()