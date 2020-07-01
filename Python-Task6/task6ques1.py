def speedCheck(speedOfVechile):
    demritPoint=0
    if(speedOfVechile<70):
        print("ok")
    else:
            differenceSpeed=speedOfVechile-70
            demritPoint=differenceSpeed/5
            if (demritPoint > 12):
                print("License suspended")
            else:
                print("Point: ",int(demritPoint))
speedOfVechile=int(input("Enter the speed of vechile"))
speedCheck(speedOfVechile)

