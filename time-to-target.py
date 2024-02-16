import math

cd = 0.03
dist1 = 0
dist2 = 0
speed1 = 0.3048000000000021701760000000154516531200001100157702144007833122* int(input("what is your first arrow's speed in fps?"))
time1 = 0
time2 = 0
target = int(input("how far is your target in meters?"))
weight1 = 0.0000647989* int(input("what is your first arrow's weight in grains?"))
weight2 = 0.0000647989* int(input("what is your second arrow's weight in grains?"))

ke = 0.5*weight1*speed1*speed1
speed2=math.sqrt(ke/(0.5*weight2))

while dist1 < target:
    time1 +=0.000001
    dist1 = dist1+speed1*0.000001
    newspeed1 = speed1 - ((0.5*1.293*cd*0.0156512*speed1*speed1)/weight1)*0.000001
    speed1 = newspeed1
print("arrow 1: " + str(time1) + "s to target")

while dist2 < target:
    time2 +=0.000001
    dist2 = dist2+speed2*0.000001
    newspeed2 = speed2 - ((0.5*1.293*cd*0.0156512*speed2*speed2)/weight2)*0.000001
    speed2 = newspeed2
print("arrow 2: " + str(time2) + "s to target")