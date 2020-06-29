#taking a file object and opening it in read only type
fileRead=open('textFile.txt','r')

#storing the strings as read from file into string
stringStore=fileRead.readlines()

#printing the strings , as contents from the file, strings are displayed as nested list.
print(stringStore)

#closing the file to save memory
fileRead.close()
