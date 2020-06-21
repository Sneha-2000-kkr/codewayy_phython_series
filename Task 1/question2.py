## Program for display full name, college name, address, total marks and percentage.

### Declaration of variables
First_name = "Sneha "
Last_name = "Singh "
College_name = "Banasthali Vidyapeeth "
Address = "Tonk, Rajasthan "

###Full name using Concatenation :

Full_name = First_name + Last_name
print(Full_name)

###college name and address :

College_name_and_Address = (College_name + Address)
print("Computer Technology from ",College_name + Address)


### Marks Declaration:

Marks_COA = 90
Marks_DAA = 90
Marks_DS = 85
Marks_DBMS = 91
Marks_SP = 90

print("\nMarks of five best subject: ")
print("\n")
print("Computer organisation and Architechure\t", Marks_COA)
print("Design and Anaylsis of Algorithm\t", Marks_DAA)
print("Data Structure\t", Marks_DS)
print("Data Base Managment System\t", Marks_DBMS)
print("System Programming", Marks_SP)

Total_marks = Marks_COA + Marks_DAA + Marks_DS + Marks_DBMS + Marks_SP
print("\nTotal_marks : ",Total_marks)


### Percentage :

Total = 500
Percentage = (Total_marks / Total) * 100
print("Percentage = ",Percentage)
