#taking a file object and opening the file in writing mode
fileWrite=open('textFile.txt','w')

#using write line to write multiple strings in the file
fileWrite.writelines("hello everyone, nice to meet you,I guess you\n "
              "must not have any problem in your journey\n"
              "kindly check-in into your rooms and be on time\n"
              "for the event, we are here to celebrate a\n"
              "special occasion,I want this event to be a life\n "
              "long memory for all of us.")
              
#closing the file when its job is done to save memory.
fileWrite.close()
