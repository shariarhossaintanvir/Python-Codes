import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

# Set up the screen and turtle
screen = turtle.Screen()
screen.bgcolor('black')
t = turtle.Pen()
t.speed(0) # Fastest speed

# Draw a colorful star pattern
for x in range(360):
    t.pencolor(colors[x % 6]) # Cycle through colors
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)

# Keep the window open
turtle.done()
