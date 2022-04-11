import turtle

# Podstawowe kolory
BODY_COLOR = 'red'
GLASS_COLOR = 'skyblue'

# Główny obiekt
t = turtle.Turtle()


# Метод для рисования тела
def body():
	t.pensize(30) # Rozmiar pędzla

	t.fillcolor(BODY_COLOR) # Kolor wypełnienia
	t.begin_fill()

	# Strona prawa
	t.right(90)
	t.forward(50)
	t.right(180)
	t.circle(40, -180)
	t.right(180)
	t.forward(200)

	# Głowa
	t.right(180)
	t.circle(100, -180)

    # Strona lewa
	t.backward(20)
	t.left(15)
	t.circle(500, -20)
	t.backward(20)

	t.circle(40, -180)
	t.left(7)
	t.backward(50)

	t.up()
	t.left(90)
	t.forward(10)
	t.right(90)
	t.down()

	t.right(240)
	t.circle(50, -70)

	t.end_fill()


# Rysujemy okulary
def glass():
    # zmieniamy lokalizację
	t.up()
	t.right(230)
	t.forward(100)
	t.left(90)
	t.forward(20)
	t.right(90)
	t.down()

	# Kolor wypełnienia
	t.fillcolor(GLASS_COLOR)
	t.begin_fill()

	t.right(150)
	t.circle(90, -55)

	t.right(180)
	t.forward(1)
	t.right(180)
	t.circle(10, -65)
	t.right(180)
	t.forward(110)
	t.right(180)

	t.circle(50, -190)
	t.right(170)
	t.forward(80)

	t.right(180)
	t.circle(45, -30)

	t.end_fill()


# Rysujemy plecak
def backpack():
	t.up()
	t.right(60)
	t.forward(100)
	t.right(90)
	t.forward(75)

	t.fillcolor(BODY_COLOR)
	t.begin_fill()

	t.down()
	t.forward(30)
	t.right(255)

	t.circle(300, -30)
	t.right(260)
	t.forward(30)
	t.end_fill()


# Wywołujemy wszystkie potrzebne metody
body()
glass()
backpack()

turtle.done()