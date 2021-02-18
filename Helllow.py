import turtle

Test_turtle = turtle.Turtle()


def square():
    Test_turtle.forward(100)
    Test_turtle.right(90)
    Test_turtle.forward(100)
    Test_turtle.right(90)
    Test_turtle.forward(100)
    Test_turtle.right(90)
    Test_turtle.forward(100)


# square()
# Test_turtle.forward(100)
# square()
man_weight = 50
women_weight = 60

if man_weight > women_weight:
    square()
else:
    Test_turtle.forward(100)
