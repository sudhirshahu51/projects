import turtle, random

def tree(branchLen,t):
    c = 10
    a = random.randint(5, 10)
    b = random.randint(20, 40)
    if branchLen > 5:
        t.pensize(branchLen//2 - 3)
        t.forward(branchLen)
        t.right(b)
        tree(branchLen-a,t)
        t.left(20 + b)
        tree(branchLen-a,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.speed(0)
    tree(75,t)
    myWin.exitonclick()

main()