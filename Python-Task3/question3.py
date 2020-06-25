#printing numbers till 10 except 7 and 3 via for and while loop

#using for loop

#defining function for printing the numbers
from _ast import Continue, Break
def printingNumbers(numBer):
    if(numBer==3 or numBer==7):
        Break
    else:
        print(numBer)
for i in range(1,11):
    printingNumbers(i)
    
#using while loop

#initializing value of x and running while loop with conditional statement that value of x must not exceed 10.
    
numBer=1
while(numBer!=11):
    if(numBer==3 or numBer==7):
        numBer=numBer+1
    else:
        print(numBer)
        numBer=numBer+1
