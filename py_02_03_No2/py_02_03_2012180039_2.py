import turtle

num1 = -2
num2 = -2

turtle.pensize(3)

for i in range(1, 6+1):
    turtle.penup()
    turtle.goto((num1 * 100) - 50, -250)
    turtle.pendown()
    turtle.goto((num1 * 100) - 50, 250)
    num1 = num1 + 1
    
for i in range(1, 6+1):
    turtle.penup()
    turtle.goto(-250, (num2 * 100) - 50)
    turtle.pendown()
    turtle.goto(250, (num2 * 100 - 50))
    num2 = num2 + 1
    



