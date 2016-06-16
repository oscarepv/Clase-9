import turtle
t = turtle.Pen()
def mipoligono(size,l):
	angulo=360/l
	for x in range (0,l):
		t.forward(size)
		t.left(angulo)
tam=int(input('ingrese el tamaño del poligono: '))
l=int(input('ingrese el tamaño del poligono: '))
	
mipoligono(tam,l)

turtle.getscreen()._root.mainloop()