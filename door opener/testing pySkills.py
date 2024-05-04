#automatic door opener 
#has multiple functions:
#1. open and close door
#2. store inforamtion on wether the door is open or closed within a csv file
#3. Either open or close the door depending on the user input 
#4. Provide and error message if the door is already in the state they are trying to acheive. either <---
# ---> opened  or closed 
#5. provide an error message if the user inputs an in valid response 
#6. ask if the user wants to continue to use the program. exit if they dont continue of they do
#NOTES:  This programe accomadates users inputs regardless of the letter case they use (Y/y, N/n)
#        This Program was full created, tested and though of by Ben McAvoy without following tutorials <---
#        ---> only figuring out things through research and testing. 


#print the hello message 
print('Hello this is the automatic door opener!')

#define the twoo futions of the door. open and close. along with what they do 
def openDoor():
    print('You have successfully opened the door.')

def closeDoor():
    print('You have closed the door.')

#create a while loop in order to have the message repeat back to the user whenever they input and answer
while True:

#define the answer input as a variable 
    doorAnswer=input('Would you like to open the door? (Y/N) ')

#open and read the text file that stores the open/closed data
    fr = open('door.txt', 'r')
    fileContents = fr.read()
    fr.close()

#set up the rulex for wether or not the door opens, closes or tell user if it is already in that state 
#if the user changes the state of the door, write the new state ot teh txt file for future ref
    if 'closed' in fileContents:
        if doorAnswer == 'Y':
            openDoor()
            fw = open('door.txt', 'w')
            fw.write('opened')
            fw.close()
        elif doorAnswer  == 'y':
            openDoor()
            fw = open('door.txt', 'w')
            fw.write('opened')
            fw.close()
    
    elif 'opened' in fileContents:
        if doorAnswer == 'Y':
            print ('The door is already open.')
        elif doorAnswer  == 'y':
            print ('The door is already open.')
    
    
    
    if 'opened' in fileContents:   
        if doorAnswer == 'N':
            closeDoor()
            fw = open('door.txt', 'w')
            fw.write('closed')
            fw.close()
        elif doorAnswer == 'n':
            closeDoor()
            fw = open('door.txt', 'w')
            fw.write('closed')
            fw.close()
   
    elif 'closed' in fileContents:
        if doorAnswer == 'N':
            print ('The door is already closed.')
        elif doorAnswer  == 'n':
            print ('The door is already closed.')

#error message if user inout something other than Y/y, N/n
    else: print('You have not made a valid selection. Goodbye!')

#add the continue option for users after they have achieve the door state they wanted
    continueOption = input("Do you want to continue? (Y/N)")
    if continueOption == 'Y':
        continue 
    elif continueOption == 'y':
        continue
    elif continueOption == 'N':
        break
    elif continueOption == 'n':
        break
    
    continue


#Lesson Learnt:
# You cannot get a varible to remeber a user inout for multiple run throughs of your program it will <---
# ---> only remeber the inputs for one runthrough of the program. Therefore, to counteract this you <---
# ---> will need to create a txt file that can store the data long term and access it through <---
# ---> f = open, r, w, a, x

# THINK : once you close down your program there is nowhere directly within the pyton code that can <---
# ---> save the data long term, so why would it be able to save the data through multiple runthroughs <---
# ---> it is the same as closing down and reopening the program from the start. I THIHK****

#Mistakes...

# This was code that i thought would work. it was placed directly under the While loop. 
# This did not work as it re-wrote the txt document before the rest of the commands had ran.
# This lead to constantly getting the ' The door is already opened/closed' message.
# to fix this I baked the writing of the new door state into one genral if statement.      

""" if doorAnswer == 'Y':
        fw = open('door.txt', 'w')
        fw.write('opened')
        fw.close()
    elif doorAnswer == 'y':
        fw = open('door.txt', 'w')
        fw.write('opened')
        w.close()
    
    elif doorAnswer == 'N':
        fw = open('door.txt', 'w')
        fw.write('closed')
        fw.close()
    elif doorAnswer == 'Y':
        fw = open('door.txt', 'w')
        fw.write('opened')
        fw.close() """

#End 

