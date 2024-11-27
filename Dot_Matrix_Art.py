import turtle as tot
import random
tim = tot.Turtle()
tot.colormode(255)
tim.speed("fastest")
tim.penup()

color_list = [(218, 219, 214), (233, 235, 239), (212, 155, 87), (213, 221, 215), (220, 205, 108),
              (224, 209, 214), (187, 82, 46), (133, 144, 28), (221, 77, 128), (41, 122, 73),
              (108, 181, 220), (162, 55, 98), (19, 126, 186), (213, 114, 151), (144, 38, 21),
              (92, 31, 84), (68, 147, 131)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_dots = 100
dot_count = 0
for count in range(1, number_dots + 1):
    tim.dot(20, random.choice(color_list))
    dot_count += 1
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

display = tot.Screen()
display.exitonclick()