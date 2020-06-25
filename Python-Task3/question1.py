#1.a
#function for returning full name of the student
def myNameFunc(firstName,lastName):
    fullName=firstName + ' '+ lastName
    return(fullName)

#1.b
#function for returning total marks scored by the student in all the subjects
def totalMarksFunc(listOfMarks):
    totalMarks=sum(listOfMarks)
    return(totalMarks)

#1.c
#function for returning percentage scored by student
def percentageFunc(listofMarks,totalMaxMarks):
    totalMarks = sum(listOfMarks)
    percentageScored=(totalMarks/totalMaxMarks)*100
    return(percentageScored)

#1.d
#function for retuning grade of the student on basis of percentage scored
def gradesScored(percentageScored):
    if(int(percentageScored)>=95):
        return('A')
    elif(int(percentageScored)>=85 and int(percentageScored)<=95):
        return('B')
    elif(int(percentageScored)>=75 and int(percentageScored)<=85):
        return('C')
    elif(int(percentageScored)>=65 and int(percentageScored)<=75):
        return('D')
    else:
        return('FAILED')

#1.e
#function for calling all other functions and printing details of the student
def detailsOfStudent(firstName,lastName,listOfMarks,totalMaxMarks,percentageScored):
    print(myNameFunc(firstName,lastName ))
    print(listOfMarks)
    print("Total marked scored:", totalMarksFunc(listOfMarks))
    print("Percentage scored:", percentageFunc(listOfMarks,totalMaxMarks))
    print("Grade Scored:", gradesScored(percentageScored))


#taking required inputs from the user
firstName=str(input("Enter your first name\n"))
lastName=str(input("Enter your last name\n"))
numberOfSubjects = int(input("enter the no of subjects\n"))
maxMarkInEachSubj=int(input("enter max marks of each subject\n"))
totalMaxMarks=(numberOfSubjects*maxMarkInEachSubj)

#initilasing a empty list of containing marks scored by the student
listOfMarks = []

#inputs from user regarding marks scored by student in each subject
print("Enter the marks of each subject")
for i in range(0, numberOfSubjects):
        marksOfSubject = float(input())
        listOfMarks.append(marksOfSubject)
percentageScored=percentageFunc(listofMarks,totalMaxMarks)

#calling function to display all the details of the student
detailsOfStudent(firstName,lastName,listOfMarks,totalMaxMarks,percentageScored)

