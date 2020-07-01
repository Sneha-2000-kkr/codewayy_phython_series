def countUpperLowerCase(stringGiven):
    countUpper = 0
    countLower= 0
    for i in stringGiven:
        if (i.isupper()):
            countUpper = countUpper + 1
    print(countUpper)
    for i in stringGiven:
        if(i.islower()):
            countLower = countLower+1
    print(countLower)
stringGiven=str(input("enter the string"))
countUpperLowerCase(stringGiven)
