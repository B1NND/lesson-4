import math
import turtle
def xt(t):
  return 6 * math.sin(t) ** 3

def yt(t):
  return 4 * math.cos(t) -2 * \
          math.cos(2 * t) - \
          math.cos(3 * t) - \
          math.cos(4 * t)

t = turtle.Turtle()
t.speed(500)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)
for i in range(500):
  t.goto((xt(i) * 10, yt(i) * 20))
  t.pencolor((255-i) % 255, i % 255, (255 + i)//2%255)
  t.goto(0, 0)

t.hideturtle()
turtle.update()
turtle.mainloop()
!!!