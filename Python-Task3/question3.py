#printing numbers till 10 except 7 and 3 via for and while loop

#using for loop

#defining function for printing the numbers
from _ast import Continue, Break
def PrintingNumbers(x):
    if(x==3 or x==7):
        Break
    else:
        print(x)
for i in range(1,11):
    PrintingNumbers(i)
    
#using while loop

#initializing value of x and running while loop with conditional statement that value of x must not exceed 10.
    
x=1
while(x!=11):
    if(x==3 or x==7):
        x=x+1
    else:
        print(x)
        x=x+1
