def findType(numberGiven):
    divisorList=[]
    for i in range(1,numberGiven):
        if(numberGiven%i==0):
               divisorList.append(i)
    if(sum(divisorList)==numberGiven):
        return 0
    elif(sum(divisorList)<numberGiven):
        return -1
    elif(sum(divisorList)>numberGiven):
        return 1

numberGiven=int(input("Enter a number"))
if(findType(numberGiven)==0):
    print("Perfect")
elif(findType(numberGiven)==1):
    print("Abundunt")
elif(findType(numberGiven)==-1):
    print("Deficient")
