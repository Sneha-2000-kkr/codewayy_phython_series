First_name = "Sneha "              //declaring variable related to personal details
Last_name = "Singh "
College_name = "Banasthali Vidyapeeth "
Address = "Tonk, Rajasthan "
Full_name = First_name + Last_name
print(Full_name)
College_name_and_Address = (College_name + Address)     // printing the strings using concatenation
print("Computer Technology from ",College_name + Address)   // printing the strings using concatenation
Marks_COA = 90            // declaring variables for marks of 5 subjects
Marks_DAA = 90
Marks_DS = 85
Marks_DBMS = 91
Marks_SP = 90
print("\nMarks of five best subject: ")
print("\n")
print("Computer organisation and Architechure\t", Marks_COA)     // printing the marks of the subjects
print("Design and Anaylsis of Algorithm\t", Marks_DAA)
print("Data Structure\t", Marks_DS)
print("Data Base Managment System\t", Marks_DBMS)
print("System Programming", Marks_SP)

Total_marks = Marks_COA + Marks_DAA + Marks_DS + Marks_DBMS + Marks_SP   // computing total marks scored
print("\nTotal_marks : ",Total_marks)
Total = 500
Percentage = (Total_marks / Total) * 100    // computing percentage 
print("Percentage = ",Percentage)


