import turtle
game_python = turtle.Turtle()


def call():
    game_python.forward(100)
    game_python.right(90)
    game_python.forward(100)
    game_python.right(90)
    game_python.forward(100)
    game_python.right(90)
    game_python.forward(100)

def callback():
    game_python.forward(100)
    game_python.left(90)


call()
callback()
call()
print("I Enjoy the Full process")
