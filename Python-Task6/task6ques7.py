class NotEligibleException(Exception):
    def message(self,message):
         return(self.message)


def checkMarks(markGiven):
    try:
        if(markGiven>=90):
            return('TRUE')
        else:
            raise NotEligibleException("FALSE")
    except NotEligibleException as no:
        return no

giveMark=int(input("Enter the mark "))
print(checkMarks(giveMark))
