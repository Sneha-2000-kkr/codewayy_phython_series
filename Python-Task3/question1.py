#1.a
#function for returning full name of the student
def MyNameFunc(FirstName,LastName):
    FullName=FirstName + ' '+ LastName
    return(FullName)

#1.b
#function for returning total marks scored by the student in all the subjects
def TotalMarksFunc(ListofMarks):
    TotalMarks=sum(ListofMarks)
    return(TotalMarks)

#1.c
#function for returning percentage scored by student
def PercentageFunc(ListofMarks,TotalMaxMarks):
    TotalMarks = sum(ListofMarks)
    PercentageScored=(TotalMarks/TotalMaxMarks)*100
    return(PercentageScored)

#1.d
#function for retuning grade of the student on basis of percentage scored
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

#1.e
#function for calling all other functions and printing details of the student
def DetailsOfStudent(FirstName,LastName,ListofMarks,TotalMaxMarks,PercentageScored):
    print(MyNameFunc(FirstName,LastName ))
    print(ListofMarks)
    print("Total marked scored:", TotalMarksFunc(ListofMarks))
    print("Percentage scored:", PercentageFunc(ListofMarks,TotalMaxMarks))
    print("Grade Scored:", GradesScored(PercentageScored))


#taking required inputs from the user
FirstName=str(input("Enter your first name\n"))
LastName=str(input("Enter your last name\n"))
NumberofSubjects = int(input("enter the no of subjects\n"))
MaxMarkInEachSubj=int(input("enter max marks of each subject\n"))
TotalMaxMarks=(NumberofSubjects*MaxMarkInEachSubj)

#initilasing a empty list of containing marks scored by the student
ListofMarks = []

#inputs from user regarding marks scored by student in each subject
print("Enter the marks of each subject")
for i in range(0, NumberofSubjects):
        MarksofSubject = float(input())
        ListofMarks.append(MarksofSubject)
PercentageScored=PercentageFunc(ListofMarks,TotalMaxMarks)

#calling function to display all the details of the student
DetailsOfStudent(FirstName,LastName,ListofMarks,TotalMaxMarks,PercentageScored)

