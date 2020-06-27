#2.c
#defining function for computing and returning result on analysing two conditions with 'and' logical operator 
def logicalOperatorAndFunc(numBer1,numBer2):
    if numBer1 > 10 and numBer2 > 10: 
        print("Both the numbers are greater than 10") 
    else: 
        print("Both the numbers are smaller than 10")
    

#defining function for computing and returning result on analysing two conditions with 'or' logical operator
def logicalOperatorOrFunc(numBer1,numBer2):
   if numBer1 > 10 or numBer2 > 10: 
        print("Atleast one number is greater than 10") 
    else: 
        print("Both the numbers are smaller than 10")
    
    
#defining function for computing and returning result on analysing a condition with 'not' logical operator
def logicalOperatorNotFunc(numBer1):
   print(not(numBer1 > 5 and numBer1 < 10))
