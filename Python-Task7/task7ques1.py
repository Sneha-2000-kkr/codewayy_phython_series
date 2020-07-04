# Class defined with methods regarding students information.

class studentInfo:

    # method within class defined for displaying student's full name
    
    def fullName(self,firstName,secondName):
        self.nameGiven= firstName + " " + secondName
        print(self.nameGiven)
  
  
    # method within class defined for displaying student's college details
    
    def collegeDetail(self,collegeName,branchEnrolledIn):
        self.collegeName=collegeName
        self.branchEnrolledIn=branchEnrolledIn
        print(self.collegeName,self.branchEnrolledIn)


    # method within class defined for displaying student's marks scored 
    
    def totalMarks(self,numberOfSubj):
        self.markList=[]
        print("Enter the marks:")
        for i in range(numberOfSubj):
            markOfSubj=int(input())
            self.markList.append(markOfSubj)
        print(sum(self.markList))
        return(sum(self.markList))


    # method within class defined for displaying student's percentage scored
    
    def percentageScored(self,sumOfMarks,numberOfSubj,eachSubjTotalMark):
        self.totalMark=numberOfSubj*eachSubjTotalMark
        self.sumOfMarks=sumOfMarks
        self.percentScored=float((self.sumOfMarks/self.totalMark)*100)
        print(self.percentScored)
        return(self.percentScored)


    # method within class defined for displaying student's grade
    
    def gradeAwarded(self,percentScored):
        if(int(percentScored)>90):
            print("A")
        elif (int(percentScored) > 80 and int(percentScored)< 89):
            print("B")
        elif (int(percentScored) > 70 and int(percentScored)< 79):
            print("C")
        elif(int(percentScored)>39 and int(percentScored)<69):
             print("D")
        elif (int(percentScored) < 40):
            print("FAILED")


# list of objects of class
studentObject=[]

#creating objects
for i in range(5):
    studentObject.append(studentInfo())
    
# taking required informations from the user and invoking desired methods in the class    
for i in studentObject:

    print("\n\nEnter details of student")
    
    print("Enter first and second name of student")
    firstName=str(input())
    secondName=str(input())
    i.fullName(firstName,secondName)
    
    
    print("Enter college name and branch")
    collageName=str(input())
    branchEnrolled=str(input())
    i.collegeDetail(collageName,branchEnrolled)
    
    
    print("Enter number of Subjects")
    numberOfSubj=int(input())
    sumMarks=i.totalMarks(numberOfSubj)
    
    
    print("Max marks in each subj")
    eachSubjTotalMark=int(input())
    
    
    percentScored=i.percentageScored(sumMarks, numberOfSubj, eachSubjTotalMark)
    i.gradeAwarded(percentScored)


