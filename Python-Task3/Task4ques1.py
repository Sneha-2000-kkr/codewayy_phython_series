# A basic code for matrix input from user
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
mat = []
mat = [[int(input()) for x in range (C)] for y in range(R)]

# For printing the matrix

for i in range(R):
    for j in range(C):
        print(mat[i][j], end = " ")
    print()

def isPrime(numberTaken):
    if numberTaken > 1:
        for i in range(2, numberTaken):
            if (numberTaken % i) == 0:
                break
                return 0
        else:
            return 1

    else:
         return 0

print("Prime numbers in the matrix")
for i in range(R):
    for j in range(C):
        if(isPrime(mat[i][j])):
            print(mat[i][j])

