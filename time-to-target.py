dist = 0
speed = 0.3048000000000021701760000000154516531200001100157702144007833122* int(input("what is your arrow speed in fps?"))
time = 0
target = int(input("how far is your target in meters?"))
weight = 0.0000647989* int(input("what is your arrow weight in grains?"))

while dist < target:
    time +=0.001
    dist = dist+speed*0.001
    newspeed = speed - ((0.5*1.293*0.05*0.016*(speed)^2)/weight)