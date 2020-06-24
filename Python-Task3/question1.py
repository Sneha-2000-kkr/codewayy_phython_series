def MyNameFunc(FirstName,LastName):
    FullName=FirstName + ' '+ LastName
    return(FullName)


def TotalMarksFunc(ListofMarks):
    TotalMarks=sum(ListofMarks)
    return(TotalMarks)

def PercentageFunc(ListofMarks,TotalMaxMarks):
    TotalMarks = sum(ListofMarks)
    PercentageScored=(TotalMarks/TotalMaxMarks)*100
    return(PercentageScored)

def GradesScored(PercentageScored):
    if(int(PercentageScored)>=95):
        return('A')
    elif(int(PercentageScored)>=85 and int(PercentageScored)<=95):
        return('B')
    elif(int(PercentageScored)>=75 and int(PercentageScored)<=85):
        return('C')
    elif(int(PercentageScored)>=65 and int(PercentageScored)<=75):
        return('D')
    else:
        return('FAILED')

def DetailsOfStudent(FirstName,LastName,ListofMarks,TotalMaxMarks,PercentageScored):
    print(MyNameFunc(FirstName,LastName ))
    print(ListofMarks)
    print("Total marked scored:", TotalMarksFunc(ListofMarks))
    print("Percentage scored:", PercentageFunc(ListofMarks,TotalMaxMarks))
    print("Grade Scored:", GradesScored(PercentageScored))



FirstName=str(input("Enter your first name\n"))
LastName=str(input("Enter your last name\n"))
NumberofSubjects = int(input("enter the no of subjects\n"))
MaxMarkInEachSubj=int(input("enter max marks of each subject\n"))
TotalMaxMarks=(NumberofSubjects*MaxMarkInEachSubj)
ListofMarks = []
print("Enter the marks of each subject")
for i in range(0, NumberofSubjects):
        MarksofSubject = float(input())
        ListofMarks.append(MarksofSubject)
PercentageScored=PercentageFunc(ListofMarks,TotalMaxMarks)
DetailsOfStudent(FirstName,LastName,ListofMarks,TotalMaxMarks,PercentageScored)

