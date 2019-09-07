import Robot as robot
from time import sleep

r4 = robot.Robot("four")

t = 1
r4.forward(t)
sleep(2)

r4.backward(t)
sleep(2)

r4.left(t)
sleep(2)

r4.right(t)
sleep(2)

r4.delete()
