# function for returnig values for grades
def gradeCal(grade):
    if (grade == "A"):
        return 4
    elif (grade == "B"):
        return 3
    elif (grade == "C"):
        return 2
    elif (grade == "D"):
        return 1
    elif (grade == "F"):
        return 0

# person class for storing name and Id of student
class personClass:
    def __init__(self):
        self.fullName=personInfo
    def get_name(self):
        for i in self.fullName:
            print(str(i.get('Name'))+"     "+str(i.get('studentID')))


# student class, inheriting person class it is used to store all students information including Student Id,
#first name, last name, number of courses enrolled, paid for tuition or not, list of courses enrolled, and
#list courses grade

class studentCLass(personClass):
    def __init__(self):
        personClass.__init__(self)
        self.students=studentInfo
        self.e=[]
        self.f=[]
        self.sumOfCredits = []
        self.cgpaList = []
        self.tutionFeeList=[]

    def get_courseOptCheck(self):
        for i in self.students:
            if(len(i.get('course opt'))>6):
                print("Sorry!!! you cannot opt for more than 6 courses")

    def set_cgpa(self):
        for i in self.students:
            self.gradeList = []
            for j in i.get('grade'):
                self.gradeList.append(gradeCal(j))

            self.e.append(self.gradeList)
            
        for i in self.students:
            self.creditList=[]
            for j in i.get('course opt'):
                self.creditList.append(j.get('credit'))
            self.f.append(self.creditList)
        

    def get_cgpa(self):
        output = [[a * b for a, b in zip(*l)] for l in zip(self.e, self.f)]
        d=[]
        for i in self.f:
            self.sumOfCredits.append(sum(i))
       
        for i in output:
            d.append(sum(i))
        
        for i in range(len(d)):
            self.cgpaList.append(d[i]/self.sumOfCredits[i])
        

    def set_tutionFee(self):
        for i in self.sumOfCredits:
            self.tutionFeeList.append(i*500)
        

    def get_totalInfo(self):
        for i in range(len(self.students)):
            print(self.students[i].get('name'),self.students[i].get('studentID'))
            for j in self.students[i].get('course opt'):
                print(j.get('course Id'),j.get('course Name'),j.get('credit'))
            print("GPA: ",self.cgpaList[i])
            print("Tution Fee: ",str(self.tutionFeeList[i])+" baht")
            print("\n")

    def get_feeBasedInfo(self):
        for i in range(len(self.students)):
             if(self.students[i].get('tutionFeePaid')=="No"):
                 print(self.students[i].get('name'),self.students[i].get('studentID'))
                 print("you need to pay the tution fee of "+str(self.tutionFeeList[i])+" baht")
             else:
                 print(self.students[i].get('name'), self.students[i].get('studentID'))
                 for j in self.students[i].get('course opt'):
                     print(j.get('course Id'), j.get('course Name'), j.get('credit'))
                 print("GPA: ", self.cgpaList[i])
                 print("Tution Fee: ", str(self.tutionFeeList[i]) + " baht")
                 print("\n")


# class course for storing information about a course including cousre Id, course name, and course credits.
class coursetClass:
    def __init__(self):
        self.corses=courseInfo
        
    def get_courses(self):
        for i in self.corses:
          print(str(i.get('course Id'))+"        "+str(i.get('course Name'))+"  "+str(i.get('credit')))



# defining menu driven function 
def mainFunction():

      print("MENU")
      print("1.List Courses")
      print("2.List Students")
      print("3.List Students and Enrollment")
      print("4.Grade Report")
      print("-1.Exit")
      choiceOFUser=int(input("Enter your choice"))
      if(choiceOFUser==1):
               c = coursetClass()
               print("Course ID   Course Name          Credit")
               c.get_courses()

      elif(choiceOFUser==2):
              p = personClass()
              print("NAME        ID")
              p.get_name()

      elif(choiceOFUser==3):
              s = studentCLass()
              s.set_cgpa()
              s.get_cgpa()
              s.set_tutionFee()
              s.get_totalInfo()

      elif(choiceOFUser==4):
              s = studentCLass()
              s.set_cgpa()
              s.get_cgpa()
              s.set_tutionFee()
              s.get_feeBasedInfo()

      elif(choiceOFUser==-1):
              print("Exist!!")


#calling main function 
mainFunction()



# Data used in code
personInfo=[{'Name':'John Wayn','studentID':12345},
            {'Name':'Jane March','studentID':12346},
            {'Name':'Marry Dolphin','studentID':12347},
            ]

courseInfo=[{'course Id':1234,'course Name':'Object-Oriented in C++','credit':3},
            {'course Id':1235,'course Name':'Financial Engineering','credit':3},
            {'course Id':1236,'course Name':'Discrete Mathamatics','credit':3},
            {'course Id':1237,'course Name':'Intro Social Science','credit':2},
            {'course Id':1238,'course Name':'Intro Linear Algebra','credit':3},
            {'course Id':1239,'course Name':'Fundamental English','credit':2},
            {'course Id':1240,'course Name':'Fundamental Japanese','credit':2},
            ]

studentInfo=[{'studentID':12345,'name':'John Wayn','course opt':[courseInfo[0], courseInfo[1], courseInfo[5], courseInfo[6]],
              'grade':['A', 'B', 'B', 'A'],'tutionFeePaid':'Yes'},
            {'studentID':12346,'name':'Jane March','course opt':[courseInfo[1], courseInfo[2], courseInfo[4], courseInfo[5], courseInfo[6]],
              'grade':['A', 'B', 'B', 'C', 'D'],'tutionFeePaid':'Yes'} ,
            {'studentID':12347,'name':'Marry Dolphin','course opt':[courseInfo[0], courseInfo[3], courseInfo[4],courseInfo[5], courseInfo[6]],
              'grade':['C', 'B', 'C', 'A', 'B'],'tutionFeePaid':'No'}]


