'''
Name: Catherine Wu
Student ID: 20099368
Date last modified: November 15th, 2018

User Interface
This program runs the user interface of the BikeShare Program. It shows all the functionalities
of the program but they do not run on real data.
The test data is created in the first readData function and stored to be used
in all the other functions. 
'''

'''This function return some random test data to be used throughout interface '''
def readData():
    return [[1, 'station1', 1.0, 1.0, 100, 50, 50], [2, 'station2', 2.0, 2.0, 200, 40, 160],\
            [3, 'station3', 3.0, 3.0, 30, 30, 0]]
    
                                                                                            
'''This function asks the user for the input of their station ID number
call this function before every task where an ID number is needed
ensures the user inputs a value which is found in the data list'''
def getStationID(stationList):
    valid = False
    while not valid:
        idInput = int(input("Enter the ID number for the station in which you are interested: "))
            
        for i in range(len(stationList)):
            if idInput in stationList[i]:
                valid = True
                print ()
                return idInput

        print ()
        print ("That is not a valid station ID. Please try again. Use an integer from 1-3.")


'''This function prints and returns all data values of a user-requested station.           
stationID is the user input number indicating the station in which they are interested.
stationList is the list of lists containing all of the station data'''
def stationInfo(stationID, stationList):
    
    stationData = []
    
    #search through the entire station data for the correct station based on ID
    for i in range(len(stationList)):
        if stationID in stationList[i]:
            #iterate through each data value of the correct station and append to
            #a list to be printed to the user
            for j in range(len(stationList[i])):
                stationData.append(stationList[i][j])

                
    #print information to the user
    print ("Below is the information for station", stationID)
    print ()
            
    print("Station Name:", stationData[1])
    print("Latitude:", stationData[2])
    print("Longitude:", stationData[3])
    print("Capacity:", stationData[4])
    print("Number of bikes available:", stationData[5])
    print("Number of docks available:", stationData[6])

    return stationData


'''This function checks a requested station in the data list for available bikes.
stationID is the user input number indicating the station in which they are interested
stationList is the list of lists containing all of the station data'''
def isBikeAvailable(stationID, stationList):

    #search through the entire station data for the correct station based on ID
    for i in range(len(stationList)):
            if stationID in stationList[i]:
                #store the value for number of available bikes at the requested station
                numBikes = stationList[i][5]

    return numBikes


'''This function checks a requested station in the data list for available docks.
stationID is the user input number indicating the station in which they are interested.
stationList is the list of lists containing all of the station data '''
def isDockAvailable(stationID, stationList):

    #search through the entire station data for the correct station based on ID
    for i in range(len(stationList)):
            if stationID in stationList[i]:
                #store the value for number of available docks at the requested station
                numDocks = stationList[i][6]

    return numDocks


'''This function searches through the data list for stations with 1+ available bikes.
The station names and # of available bikes are appended to a new list and sorted from
most available bikes to least. The function returns this list.
stationList is the list of lists containing all of the station data'''
def bikeAvailableStations(stationList):

    #list of stations with available bikes
    bikeAvailability = []
    
    for i in range(len(stationList)):
        #check for no available bikes
        if stationList[i][5] > 0:
            #append name and # of available bikes
            bikeAvailability.append(stationList[i][1:6:4])

    #must sort list from most bikes to least in actual implementation

    return bikeAvailability


'''This function searches through the data list for stations with 0 available docks.
The station names are appended to a new list which is returned by the function.
stationList is the list of lists containing all of the station data'''
def fullCapacityStations(stationList):

    #list of stations at capacity
    capacity = []

    for i in range(len(stationList)):
        #check for no available docks
        if stationList[i][6] == 0:
            #append name 
            capacity.append(stationList[i][1])

    return capacity


'''This function allows users to rent some number of bikes from a requested station.
The station is checked for anough bike available and the data values are appropriately
increased/decreased.
stationList is the list of lists containing all of the station data
stationID is the station from which they want to rent 
'''
def rentBike(stationList, stationID):

    invalidInput = True
    while invalidInput:
        #ensure they enter a numerical character, not a string
        try:
            numBikes = int(input("Please enter the number of bicycles you wish to rent: "))
            invalidInput = False

        except:
            print("That is invalid. Please enter an integer value (ex. 1)")
            print ()

    #must check through the data list for bike availability and change data values
    #in final implementation

    #user interaction       
    if numBikes == 1:
        print("You have rented", numBikes,  "bicycles")
    else:
        print("You have rented", numBikes, "bicycles")

    return None


'''This function allows users to return some number of bikes to a requested station.
The station is checked for enough dock availability and the data values are appropriately
increased/decreased.
stationList is the list of lists containing all of the station data
stationID is the station to which they want to return the bikes'''
def returnBike(stationList, stationID):

    invalidInput = True
    
    while invalidInput:
        #ensure they enter a numerical character, not a string
        try:
            numReturns = int(input("Please enter the number of bicycles you wish to return: "))
            invalidInput = False

        except:
            print("That is invalid. Please enter an integer value (ex. 1)")
            print ()

    #must check for available docks and change data values in final implementation

    #user interaction
    if numReturns == 1:
        print ()
        print("You have successfully returned", numReturns,  "bicycle.\
 Thank you for using the Bikeshare services.")
    else:
        print ()
        print("You have successfully returned", numReturns, "bicycles.\
 Thank you for using the Bikeshare services.")

    return None


'''This function gives users basic directions to go from one station to another.
Ths user must input both station IDs before using this functionality.
The two station parameters are user inputs. stationList is the list of lists containing all station data'''
def giveDirections(station1, station2, stationList):

    #must find difference between longitude and latitude for final implementation

    #inform user to travel to the destination
    #will include actula directions in final implementation
    print("Travel to get from Station", station1, "to Station", station2)
    return None


'''This function prints the menu of tasks the program is capable of performing
The user is also asked for input on what functionality they would like to be executed'''
def menu():

    print("What would like to do today?")
    print("1 Look up information about a station")
    print("2 Check for available bicycles")
    print("3 Check for available bicycle docks")
    print("4 Rent a bicycle")
    print("5 Return a bicycle")
    print("6 Get directions to another station")
    print("7 Find stations at full capacity")
    print ()
        
    #get user input
    userChoice = input("Please enter the number corresponding to the functionality\
 you would like to check out!\n")

    return userChoice


'''This function is called at the end of each loop of the main function.
User is asked if they wish to continue using the program.
'''  
def repeatProgram():
    
    checkRepeat = True

    #loop to ensure user input is 'y' or 'n'
    while checkRepeat:
            repeat = input("If you wish to return to the menu, enter 'y'. \
If you wish to exit the program, enter 'n'\n")

            #if user wishes to exit, return that information to main function
            if repeat == 'n':
                print ()
                print ("Thank you for using the Toronto Bikeshare Program App! We hope \
you enjoy your cycling experience!")
                return False
            
            #catch any characters which are not correct
            elif repeat != 'y':
                print ("That was not a valid character. Try again.")

            #if user wishes to return to main menu, return info to main function
            else:
                print ()
                return True
            

'''This is the main function.
Based on the user choice made in the menu function, user inputs are retrieved
and other functions are called to execute the task.
It runs a loop to allow user to return to the main menu after each task,
based on user input received from repeatProgram function.'''
def main():

    #keeps loop running
    running = True

    #stores the data in a variable to be used as a parameter for the other functions
    stationList = readData()

    #opening message to user
    print("Welcome to the Toronto Bikeshare Program! We are delighted to offer\
 rental bicycles for you to use as you travel around our wonderful city!")
    print ()

    #loop which executes function calls based on user's input choice
    #loads the menu at the beginning of each loop
    while running:
        taskNum = menu()

        #big 'if statement' to execute different functions for each possible input value
        if taskNum == '1':
            print("You have selected to look up information about a station")            
            print ()
            stationID = getStationID(stationList)
            
            stationData = stationInfo(stationID, stationList)
           
        elif taskNum == '2':
            print("You have selected to check for bicycle availability")
            #two options are given to user when they choose to check for bike availability
            choiceCheck = input("To check general availability enter '1'. To check availability \
at a specific station, enter '2'\n")
            
            if choiceCheck == '1':
                stationAvailability = bikeAvailableStations(stationList)
                #all stations with available bikes are printed in a sorted list
                print("Below are listed the stations with available bikes")

                for i in range(len(stationAvailability)):
                    print (stationAvailability[i])

            elif choiceCheck == '2':
                stationID = getStationID(stationList)
                #user requested station is checked for available bikes
                print("There are",isBikeAvailable(stationID, stationList), \
                      "bicycles available at Station", stationID)

            #catch incorrect input values from user
            else:                
                print ("You have made an invalid input value. Please return \
to the menu and retry this functionality")

        elif taskNum == '3':
            print("You have selected to check for bicycle dock availability")
            print()
            #request station ID from user
            stationID = getStationID(stationList)

            print("There are",isDockAvailable(stationID, stationList), \
                    "bicycle docks available at Station", stationID)

        elif taskNum == '4':
            print("You have selected to rent a bicycle")
            print()
            #request station ID from user
            stationID = getStationID(stationList)
            
            rentBike(stationList, stationID)
            
        elif taskNum == '5':
            print("You have selected to return a bicycle")
            print()
            #request station ID from user
            stationID = getStationID(stationList)

            returnBike(stationList, stationID)

        elif taskNum == '6':
            print("You have selected to get directions to another station")
            print()
            #request station ID from user for both stations and store in parameter values
            station1 = int(input("Enter the ID number for the station where you are currently situated: "))
            station2 = getStationID(stationList)

            giveDirections(station1,station2,stationList)

        elif taskNum == '7':
            print("You have selected to see a list of stations at full capacity")

            atCapacity = fullCapacityStations(stationList)
            print()
            print("Below is a list of stations which are at full capacity (have no available docks):")

            #print the station names in a list order(one underneath the other)
            for i in range(len(atCapacity)):
                print(atCapacity[i])

        #ensure the user doesn't cause an error by inputing an invalid character
        else:
            print("You have not made a valid selection.\
 Make sure to enter only a numerical value between 1 and 7.")

        print()
        #call repeatProgram function to ask user if they wish to continue
        #after completing the task
        running = repeatProgram()

      
#run program!!    
main()
    

