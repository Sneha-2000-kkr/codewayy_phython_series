# Class defined with methods regarding students information.

class studentInfo:

    # constructor for initializing the variables
    def __init__(self,firstName,secondName,collegeName,branchEnrolledIn,numberOfSubj,eachSubjTotalMark):
        self.firstName=firstName
        self.secondName=secondName
        self.collegeName=collegeName
        self.branchEnrolledIn=branchEnrolledIn
        self.numberOfSubj=numberOfSubj
        self.eachSubjTotalMark=eachSubjTotalMark


    # method within class defined for displaying student's full name

    def fullName(self):
        self.nameGiven = self.firstName + " " + self.secondName
        print(self.nameGiven)

    # method within class defined for displaying student's college details

    def collegeDetail(self):
        print(self.collegeName, self.branchEnrolledIn)

    # method within class defined for displaying student's marks scored

    def totalMarks(self):
        self.markList = []
        print("Enter the marks:")
        for i in range(self.numberOfSubj):
            markOfSubj = int(input())
            self.markList.append(markOfSubj)
        print("Total markes scored :",sum(self.markList))
        return (sum(self.markList))

    # method within class defined for displaying student's percentage scored

    def percentageScored(self, sumOfMarks):
        self.totalMark = self.numberOfSubj * self.eachSubjTotalMark
        self.sumOfMarks = sumOfMarks
        self.percentScored = float((self.sumOfMarks / self.totalMark) * 100)
        print("Percentage Scored:",self.percentScored)
        return (self.percentScored)

    # method within class defined for displaying student's grade

    def gradeAwarded(self, percentScored):
        if (int(percentScored) >= 90):
            print("Grade awarded is A\n\n")
        elif (int(percentScored) >= 80 and int(percentScored) <= 89):
            print("Grade awarded is B\n\n")
        elif (int(percentScored) >= 70 and int(percentScored) <= 79):
            print("Grade awarded is C\n\n")
        elif (int(percentScored) >= 39 and int(percentScored) <= 69):
            print("Grade awarded is D\n\n")
        elif (int(percentScored) <= 40):
            print("Sorry!! YOU FAILED\n\n")


# list of objects of class
studentObject = []
studentNo=1
# creating objects and taking required informations from the user and invoking desired methods in the class
for i in range(5):
    print("Details of student ",studentNo)
    print("Enter first and second name of student")
    firstName = str(input())
    secondName = str(input())
    print("Enter college name and branch")
    collageName = str(input())
    branchEnrolled = str(input())
    print("Enter number of Subjects")
    numberOfSubj = int(input())
    print("Max marks in each subj")
    eachSubjTotalMark = int(input())
    studentObject.append(studentInfo(firstName,secondName,collageName, branchEnrolled,numberOfSubj,eachSubjTotalMark))
    studentNo+=1

# invoking the methods
for i in studentObject:
    i.fullName()
    i.collegeDetail()
    totalMarks=i.totalMarks()
    percentScored=i.percentageScored(totalMarks)
    i.gradeAwarded(percentScored)




