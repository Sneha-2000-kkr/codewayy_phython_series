#2.c
#defining function for computing and returning result on analysing two conditions with 'and' logical operator 
def logicalOperatorAndFunc(numBer1,numBer2):
    if(numBer1=='True'):
        if(numBer2=='True'):
            return ('True')
    else:
        return ('False')
    

#defining function for computing and returning result on analysing two conditions with 'or' logical operator
def logicalOperatorOrFunc(numBer1,numBer2):
    if(numBer1=='False'):
        if(numBer2=='False'):
            return ('False')
    else:
        return('True')
    
    
#defining function for computing and returning result on analysing a condition with 'not' logical operator
def logicalOperatorNotFunc(numBer1):
    if(numBer1=='True'):
        return ('False')
    else:
        return ('True')
