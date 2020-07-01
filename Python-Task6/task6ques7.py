# User defined Exception
class NotEligibleException(Exception):
    def message(self,message):
         return(self.message)

# Checking for marks 
def checkMarks(markGiven):
    try:
        if(markGiven>=90):
            return('TRUE')
        else:
            raise NotEligibleException("FALSE")
    except NotEligibleException as no:
        return no

 # taking marks as input from the user
giveMark=int(input("Enter the mark "))
print(checkMarks(giveMark))
