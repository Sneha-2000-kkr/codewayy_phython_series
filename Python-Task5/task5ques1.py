#taking a number input from the user and if its not positive number value error message has been raised

try:
     takeNumber= int(input("Enter a positive integer: "))
     if takeNumber <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as positiveNumber:
       print(positiveNumber)
       
# if the number is positive displaying the result accordingly
finally:
    if(takeNumber>=0):
      print(str(takeNumber)+" is a positive number")
