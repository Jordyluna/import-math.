import math 
from turtle import*

def flowera(k):
    return 15*math.sin(k)**3
def flowerb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
     math.cos(4*k)
speed (-4000)
bgcolor("black")
for i in range(60000):
    goto(flowera(i)*10, flowerb(i)*10)
    for j in range(5):
        color("red")
    goto (0,0)
done()