'''
Name: Catherine Wu
Student ID: 20099368
Date last modified: November 27th, 2018

Bike Share Program. Project Implementation.

This program models an app for the Toronto Bikeshare Program.
Data is sourced from the url "http://research.cs.queensu.ca/home/cords2/bikes.txt".

This program interacts with users, providing several functionalities
including renting, returning, searching information, giving directions, and more!
'''

import urllib.request

'''This function gets the data from the given url and splits it into lines of text'''
def readData():
    link = "http://research.cs.queensu.ca/home/cords2/bikes.txt"
    f = urllib.request.urlopen(link)
    myfile = f.readlines()
    return myfile


'''This function organizes the data into a list of lists. Each list contains
the information for one station, beginning with ID number.'''
def organizeData():
    myfile = readData()
    bikeData = []
    for line in myfile:
        bikeData.append(line.decode("utf/8").strip().split('\t'))

    #remove the title headings from the list
    bikeData = bikeData[1:]
    
    return bikeData


'''This function casts the data to the proper data types.
This ensures that for later functions, the numbers will be able to be manipulated
mathematically'''
def setDataType():
    stationList = organizeData()
    
    for i in range(len(stationList)):     
        #lat and long to float values
        stationList[i][2], stationList[i][3] = float(stationList[i][2]),float(stationList[i][3])
        #capacity, num available to int values
        stationList[i][4], stationList[i][5], stationList[i][6] = int(stationList[i][4]), int(stationList[i][5]), int(stationList[i][6])

    return stationList


'''This function asks the user for the input of their station ID number
call this function before every task where an ID number is needed
ensures the user inputs a value which is found in the data list'''
def getStationID(stationList):

    valid = False
    while not valid:
        idInput = input("Enter the station ID number for the station in which you are interested: ")

        #search for the ID in the data and return it
        for i in range(len(stationList)):
            if idInput in stationList[i]:
                valid = True
                print ()
                return idInput

        #if the ID isn't found in the data, prompt user to try another number
        print()
        print("That is not a valid station ID. Please try again.\n")

        
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
    
    return stationData


'''This function receives information from stationInfo and prints it out
for the user to see'''
def printStationInfo(stationID, stationList):

    stationData = stationInfo(stationID, stationList)
    
    if stationData != []:
        print("Below is the information for station", stationID)
        print()
        print("Station Name:", stationData[1])
        print("Latitude:", stationData[2])
        print("Longitude:", stationData[3])
        print("Capacity:", stationData[4])
        print("Number of bikes available:", stationData[5])
        print("Number of docks available:", stationData[6])

    else:
        print("Sorry, the station ID is invalid.")
        
    return None


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
    bikeAvail = []
   
    for i in range(len(stationList)):
        #check for no available bikes
        if stationList[i][5] > 0:
            #append name and # of available bikes
            bikeAvail.append(stationList[i][1:6:4])

    #sort list
    for i in range(len(bikeAvail)):
        #set minimum value to be the first value in the list
        max = i
        j = max + 1
        #find the index of the maximum value in the list from i+1 to end
        while j < len(bikeAvail):
            if bikeAvail[j][1] > bikeAvail[max][1]:
                max = j
            j = j + 1
        if (max != i):
            #swap the values
            bikeAvail[max], bikeAvail[i] = bikeAvail[i], bikeAvail[max]

    return bikeAvail


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


'''This function preceeds the rentBike function to interact with the user,
receiving and returning the number of bikes they wish to rent'''
def getNumRentals():
    
    invalidInput = True
    while invalidInput:
        #ensure they enter a numerical character, not a string
        try:
            numBikes = int(input("Please enter the number of bicycles you wish to rent: "))
            invalidInput = False

        except:
            print("That is invalid. Please enter an integer value (ex. 1)\n")

    return numBikes


'''This function allows users to rent some number of bikes from a requested station.
The station is checked for anough bike available and the data values are appropriately
increased/decreased.
stationList is the list of lists containing all of the station data
stationID is the station from which they want to rent 
'''
def rentBike(stationList, stationID, numBikes):

    for i in range(len(stationList)):
        if stationID == stationList[i][0]:
            if stationList[i][5] >= numBikes:
                #decrease number of bikes available
                stationList[i][5] -= numBikes
                #increase number of docs available
                stationList[i][6] += numBikes

                #user interaction       
                if numBikes == 1:
                    print()
                    print("You have rented", numBikes,  "bicycles")
                else:
                    print()
                    print("You have rented", numBikes, "bicycles")
            
            else:
                print()
                print("Sorry, there are not enough bikes available at this station.")
                
    return stationList


'''This function preceeds the rentBike function to interact with the user,
receiving and returning the number of bikes they wish to rent'''
def getNumReturns():

    invalidInput = True     
    while invalidInput:
        #ensure they enter a numerical character, not a string
        try:
            numReturns = int(input("Please enter the number of bicycles you wish to return: "))
            invalidInput = False

        except:
            print("That is invalid. Please enter an integer value (ex. 1)\n")
            
    return numReturns

            
'''This function allows users to return some number of bikes to a requested station.
The station is checked for enough dock availability and the data values are appropriately
increased/decreased.
stationList is the list of lists containing all of the station data
stationID is the station to which they want to return the bikes'''
def returnBike(stationList, stationID, numReturns):

    #check for available docks and change data values accordingly
    for i in range(len(stationList)):
        if stationID == stationList[i][0]:
            if stationList[i][6] >= numReturns:
                #decrease number of bikes available
                stationList[i][6] -= numReturns
                #increase number of docs available
                stationList[i][5] += numReturns

                #user interaction
                if numReturns == 1:
                    print()
                    print("You have successfully returned", numReturns,  "bicycle.\
 Thank you for using the Bikeshare services.")
                else:
                    print()
                    print("You have successfully returned", numReturns, "bicycles.\
 Thank you for using the Bikeshare services.")
           
            else:
                print()
                print("Sorry, there are not enough docks available at this station")
                
    return stationList


'''This function gives users basic directions to go from one station to another.
Ths user must input both station IDs before using this functionality.
The two station parameters are user inputs. stationList is the list of lists containing all station data'''
def giveDirections(start, destination, stationList):

    #initiate variables
    directionNS = 'south'
    directionEW = 'west'
    lat1,lat2,long1,long2 = 0,0,0,0

    #find and store the latitiudes and longitudes of the two stations
    for i in range(len(stationList)):
        if start == stationList[i][0]:
            lat1 = stationList[i][2]
            long1 = stationList[i][3]
        if destination == stationList[i][0]:
            lat2 = stationList[i][2]
            long2 = stationList[i][3]

    #determine the directions needed to travel
    if lat1 < lat2:
        directionNS = 'north'
    if long1 < long2:
        directionEW = 'east'

    #handle case where user enters same station for start and end
    if lat1 == lat2 and long1 == long2:
        print("You have entered the same station twice")
    else:
        #inform user to travel to the destination
        print("Travel", directionNS, directionEW, "to get from Station", start, "to Station", destination)

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
    print()
        
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
                print()
                print("Thank you for using the Toronto Bikeshare Program App! We hope \
you enjoy your cycling experience!")
                return False
            
            #catch any characters which are not correct
            elif repeat != 'y':
                print()
                print("That was not a valid character. Try again.")

            #if user wishes to return to main menu, return info to main function
            else:
                print()
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
    stationList = setDataType() 

    #opening message to user
    print("Welcome to the Toronto Bikeshare Program! We are delighted to offer\
 rental bicycles for you to use as you travel around our wonderful city!\n")

    #loop which executes function calls based on user's input choice
    #loads the menu at the beginning of each loop
    while running:
        taskNum = menu()

        #big 'if statement' to execute different functions for each possible input value
        if taskNum == '1':
            print("You have selected to look up information about a station\n")
            
            stationID = getStationID(stationList)

            printStationInfo(stationID,stationList)
           
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
            print("You have selected to check for bicycle dock availability\n")
            
            #request station ID from user
            stationID = getStationID(stationList)

            print("There are",isDockAvailable(stationID, stationList), \
                    "bicycle docks available at Station", stationID)

        elif taskNum == '4':
            print("You have selected to rent a bicycle\n")
            
            #request station ID and 3 of bikes to rent from user
            stationID = getStationID(stationList)
            numBikes = getNumRentals()
            
            stationList = rentBike(stationList, stationID, numBikes)
            
        elif taskNum == '5':
            print("You have selected to return a bicycle\n")

            #request station ID and # of bikes to return from user
            stationID = getStationID(stationList)
            numReturns = getNumReturns()
            
            stationList = returnBike(stationList, stationID, numReturns)

        elif taskNum == '6':
            print("You have selected to get directions to another station\n")

            #request station ID from user for both stations and store in parameter values
            station1 = getStationID(stationList)
            station2 = getStationID(stationList)

            giveDirections(station1,station2,stationList)

        elif taskNum == '7':
            print("You have selected to see a list of stations at full capacity\n")

            atCapacity = fullCapacityStations(stationList)
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


#only run main in this program file(not in the test file!)
if __name__ == '__main__':
    #run program
    main()



            
