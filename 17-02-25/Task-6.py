from turtle import *

m = 10
tracer(0)
lt(90)

for i in range (2):
    rt(120)
    fd(7 * m)
rt (300)
for i in range(2):
    rt(120)
    fd(7 * m)
up()
for x in range (-20,20):
    for y in range(-20,20):
        goto(m*x, m*y)
        dot(3)

done()


