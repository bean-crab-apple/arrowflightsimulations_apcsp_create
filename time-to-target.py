import math

def flightsim(speed,weight,cd,target):
    dist = 0
    time = 0
    while dist < target:
        time +=0.000001
        dist = dist+speed*0.000001
        newspeed = speed - ((0.5*1.293*cd*0.0156512*speed*speed)/weight1)*0.000001
        speed = newspeed
    finalparams = [speed,time]
    return finalparams

def findcd(speedbow,speedtarget,weight,target):
    cdmatch = False
    testcd = 0
    mode = 1
    step = 0.001
    while cdmatch == False:
        cdtestfinalparams = flightsim(speedbow,weight,testcd,target)
        print(cdtestfinalparams[0])
        if -0.000000001 < (cdtestfinalparams[0] - speedtarget) < 0.000000001:
            cdmatch = True
            return testcd
        else:
            if mode*(cdtestfinalparams[0] - speedtarget) < 0:
                mode = (-1)*mode
                step = (-0.1)*step
                testcd = testcd+step
            else:
                testcd = testcd+step

speedbow = 0.3048000000000021701760000000154516531200001100157702144007833122* int(input("what is your first arrow's speed out of the bow in fps?"))
speedtarget = 0.3048000000000021701760000000154516531200001100157702144007833122* int(input("what is your first arrow's speed at the target in fps?"))

target = int(input("how far is your target in meters?"))
weight1 = 0.0000647989* int(input("what is your first arrow's weight in grains?"))
weight2 = 0.0000647989* int(input("what is your second arrow's weight in grains?"))

ke = 0.5*weight1*speedbow*speedbow
speed2 = math.sqrt(ke/(0.5*weight2))

cd = findcd(speedbow,speedtarget,weight1,target)

finalparams1 = flightsim(speedbow,weight1,cd,target)
finalparams2 = flightsim(speed2,weight2,cd,target)

print("arrow 1: " + str(finalparams1[1]) + "s to target")
print("arrow 2: " + str(finalparams2[1]) + "s to target")