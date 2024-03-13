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
    while cdmatch == False:
        cdtestfinalparams = flightsim(speedbow,weight,testcd,target)
        print(cdtestfinalparams[0])
        if (cdtestfinalparams[0] - speedtarget) < 0:
            cdmatch = True
        else:
            testcd+=0.001
    cdmatch = False
    while cdmatch == False:
        cdtestfinalparams = flightsim(speedbow,weight,testcd,target)
        print(cdtestfinalparams[0])
        if (cdtestfinalparams[0] - speedtarget) > 0:
            cdmatch = True
        else:
            testcd-=0.00001
    cdmatch = False
    while cdmatch == False:
        cdtestfinalparams = flightsim(speedbow,weight,testcd,target)
        print(cdtestfinalparams[0])
        if (cdtestfinalparams[0] - speedtarget) < 0:
            cdmatch = True
        else:
            testcd+=0.0000001
    cdmatch = False
    while cdmatch == False:
        cdtestfinalparams = flightsim(speedbow,weight,testcd,target)
        print(cdtestfinalparams[0])
        if (cdtestfinalparams[0] - speedtarget) > 0:
            cdmatch = True
            return testcd
        else:
            testcd-=0.000000001

speedbow = 0.3048000000000021701760000000154516531200001100157702144007833122* int(input("what is your first arrow's speed out of the bow in fps?"))
speedtarget = 0.3048000000000021701760000000154516531200001100157702144007833122* int(input("what is your first arrow's speed at the target in fps?"))

target = int(input("how far is your target in meters?"))
weight1 = 0.0000647989* int(input("what is your first arrow's weight in grains?"))
weight2 = 0.0000647989* int(input("what is your second arrow's weight in grains?"))

ke = 0.5*weight1*speedbow*speedbow
speed2 = math.sqrt(ke/(0.5*weight2))

cd = findcd(speedbow,speedtarget,weight1,target)

timefinal1 = flightsim(speedbow,weight1,cd,target)
timefinal2 = flightsim(speed2,weight2,cd,target)

print("arrow 1: " + str(timefinal1[1]) + "s to target")
print("arrow 2: " + str(timefinal2[1]) + "s to target")