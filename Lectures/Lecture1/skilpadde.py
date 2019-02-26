from turtle import *

colors = ["blue", "red", "green", "pink"]

for i in range(4):
    speed(0)
    color(colors[i])

    side=20
    penup()
    goto(10 * i,10 * i) #position cursor at the bootom right of the screen
    pendown()

    for i in range (1,150):
        forward(side)
        left(92)
        side = side + 7


    penup()
    goto(500,500)




"""
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

"""