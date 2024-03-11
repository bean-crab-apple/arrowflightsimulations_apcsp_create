import math

def flightsim(speed,weight,cd):
    dist = 0
    time = 0
    while dist1 < target:
        time +=0.000001
        dist = dist+speed*0.000001
        newspeed = speed - ((0.5*1.293*cd*0.0156512*speed1*speed1)/weight1)*0.000001
        speed = newspeed
    finalparams = [speed,time]
    return finalparams

speedbow = 0.3048000000000021701760000000154516531200001100157702144007833122* int(input("what is your first arrow's speed out of the bow in fps?"))
speedtarget = 0.3048000000000021701760000000154516531200001100157702144007833122* int(input("what is your first arrow's speed at the target in fps?"))

target = int(input("how far is your target in meters?"))
weight1 = 0.0000647989* int(input("what is your first arrow's weight in grains?"))
weight2 = 0.0000647989* int(input("what is your second arrow's weight in grains?"))

ke = 0.5*weight1*speed1*speed1
speed2=math.sqrt(ke/(0.5*weight2))

print("arrow 1: " + str(time1) + "s to target")

print("arrow 2: " + str(time2) + "s to target")