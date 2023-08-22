#---------------------
# Summer Davis
# COSC 1336
# Project 8
#---------------------
# Objective: Create a database from a text file. User will be able to
# search the database to find student profiles.
#
# Program will:
# - create a database by reading a text file of student information
# and using the information to populate a dictionary
#(The student ID will be the key and the student name will be the value)
# - ask user if they would like to search for a student (Y/N)
# - validate user input
# - if valid, display results
# - Y -> ask user to enter a student ID
#     -> generate student name and ID
#     -> ask user if they want to search again
# - N -> end program
#     -> display how many times user has searched
#---------------------

# Display the start of the project
def header ():
    print('\n')
    print('-' * 60)
    print('Search Student Information')
    print('-' * 60)

# Collect and organize all of the program tasks
def main():
    
    # Header of the project
    header()

    # Create student database
    database = readData('data.txt')

    # Search for student profile(s)
    search(database)
    
    # End of project display
    footer()


# Displays search results
def displayResult(studentID, database):
    print('\n')
    print('-' * 60)
    print('Student Query Result')
    print('-' * 60)
    
    try:
        name = database[studentID]
        print('Student Found')
        print(f'Name: {name}')
        print(f'ID: {studentID}')
        print('\n')
        
    except KeyError:
        print('Student Not Found\n')


# Searches database for student ID
def search(database):
    
    count = 0
    again = getStringData('Are you ready to search? (Y/N) ')
    
    while (again == 'Y'):

        studentID = input('Please enter a student ID: ')
        count += 1
        displayResult(studentID, database)
        again = getStringData('Are you ready to search? (Y/N) ')
       

    print(f'\nYou have searched {count} times')


# Reads a file based on delimiter
# and returns a dictionary
def readData(fileName):
    
    database = {} 
        
    dataFile = open(fileName, 'r')

    for line in dataFile:
        newLine = line.strip('\n')
        if (len(newLine) > 0):
                
            try:
                tempList = newLine.split(', ')
                key = tempList[0]
                value = tempList[1]

                database[key] = value 
                    
            except ValueError:
                continue

    dataFile.close()
        
    return database

# Get users entry of string data
def getStringData(prompt):
    while (True):
        value = input(prompt).upper()

        if (value == 'Y' or value == 'N'):
            return value
        else:
            print('\n\tError: Please enter Y or N.\n')

        
# Get users entry of ONLY float data
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value

        except ValueError: 
            print('\n\tError Msg: Non Numbers entered.\n')

# Get users entry of ONLY integer data
def getIntegerData(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value

        except ValueError: 
            print('\n\tError Msg: Non Integers entered.\n')
    
# Display the end of the project
def footer():
    print('\n')
    print('-' * 60)
    print('End of Project 8')

# Call the main function  
main()
