'''
Name: Catherine Wu
Date last modified: Nov. 27th, 2018

test all the functions bro

This program prints return values of most functions from the bike share program.

A minimum of two cases are tested per function and expected return values
are commented throughout the code.
'''

#get stuff from the program!
import bikeImplementation as bike

#random set of data with different cases
stationList = [['1', 'station1', 1.0, 1.0, 100, 0, 100], ['2', 'station2', 2.0, 2.0, 200, 20, 180],\
            ['3', 'station3', 3.0, 3.0, 30, 30, 0]]

def testReadData():
    print("NOW TESTING READING DATA")
    read_tester = bike.readData()

    #ensure data is being read and returned
    if len(read_tester) == 0:
        print("Failure to read data")
    else:
        print("Test successful\n")
        

def testOrganizeData():
    print("NOW TESTING ORGANIZING DATA")
    organize_tester = bike.organizeData()

    #ensure characters are stripped from html
    for i in range(len(organize_tester)):
        if '\t' in organize_tester[i]:
            print("Data not fully stripped")
            return None
        if len(organize_tester[i]) != 7:
            print("Missing element from data")

    #ensure the list created in this function is actually formed
    if len(organize_tester) == 0 :
        print("Failure to transfer data")
    else:
        print("Test successful\n")


def testSetDataType():
    print("NOW TESTING SETTING DATA TYPE")
    cast_tester = bike.setDataType()
    
    #ensure casting of values is successful
    for i in range(len(cast_tester)):
        if type(cast_tester[i][2]) != float or type(cast_tester[i][3]) != float:
            print(cast_tester[i])
            print("Failure to cast longitude and latitude to float")
            return None
        if type(cast_tester[i][4]) != int or type(cast_tester[i][5])\
           != int or type(cast_tester[i][6]) != int:
            print("Failure to cast integers")
            return None
        
    print("Test successful\n")
    

#includes user interface but will be testing handling incorrect entries
def testGetStationID():
    print("NOW TESTING GETTING STATION ID. Input a number between 1 and 3")
    bike.getStationID(stationList)
    print("Input a number outside range 1 to 3. Then when prompted \
to try again, use a letter, then finally a number from 1 to 3") #not in data
    bike.getStationID(stationList)#loop until proper input is received
    print("If no error message, test successful\n")
    

def testStationInfo():
    print('NOW TESTING STATION INFO')
    bike.stationInfo(1,stationList) #print info
    bike.stationInfo(500,stationList) #not in data
    print()
    print("If no error, test successful\n")
    

def testIsBikeAvailable():
    print('NOW TESTING CHECKING BIKE AVAILABLITY')
    
    available_tester = bike.isBikeAvailable(1, stationList) #0 bikes
    available_tester2 = bike.isBikeAvailable(3, stationList) #30 bikes
    if available_tester != 0 or available_tester2 != 30:
        print("Incorrect value being returned")
    else:
        print("Test successful\n")  

    
def testIsDockAvailable():
    print('NOW TESTING CHECKING DOCK AVAILABILITY')
    dock_tester = bike.isDockAvailable(1, stationList) #100 docks
    dock_tester2 = bike.isDockAvailable(3, stationList) #0 docks
    if dock_tester != 100 and dock_tester2 != 0:
        print("Incorrect value being returned")
    else:
        print("Test successful\n")
        
    
def testBikeAvailableStations():
    print('NOW TESTING STATIONS WITH AVAILABLE BIKES')
    stations_tester = bike.bikeAvailableStations(stationList)
    if len(stations_tester) == 0:
        print("Failure to determine available bikes at stations")
    if stations_tester[0][0] != 'station3':
        print("Failure to sort stations by number of availabe bikes")
    else:
        print("Test successful\n")
        

def testFullCapacityStations():
    print('NOW TESTING FULL CAPACITY STATIONS')
    capacity_tester = bike.fullCapacityStations(stationList) #only station 3

    if len(capacity_tester) == 0 or 'station3' not in capacity_tester:
        print("Failure to determine full capacity at stations")
    else:
        print("Test successful\n")
        
    
def testRentBike():
    print('NOW TESTING RENTING BIKE')
    #check for changed data values
    rent_tester = bike.rentBike(stationList,'2', 3) 
    rent_tester2 = bike.rentBike(stationList,'1',2) #no bikes

    if rent_tester[1][5] != 17 or rent_tester[1][6] != 183 :
        print("Failure to decrease available bikes and/or increase available docks.")
    else:
        print("Test successful\n")
        

def testReturnBike():
    print('NOW TESTING RETURNING BIKE')
    #check for changed data values
    return_tester = bike.returnBike(stationList,'1',10)
    return_tester2 = bike.returnBike(stationList,'3',4) #no docks

    if return_tester[0][5] != 10 or return_tester[0][6] != 90:
        print("Failure to increase available bikes and/or decrease available docks")
    else:
        print("Test successful\n")
        

def testGiveDirections():
    print('NOW TESTING GIVING DIRECTIONS')
    #opposites (NE and SW)
    bike.giveDirections('1','2',stationList) 
    bike.giveDirections('2','1',stationList)

    print("If directions printed are opposite of each other, test successful\n")
    

def testRepeat():
    print('NOW TESTING REPEATING PROGRAM')
    #try with a bunch of different characters
    bike.repeatProgram()

    print("If no error, test successful\n")


'''side note: bike.menu() is not tested because it simply prints out a list of
possible tasks that program can perform. The return value is a user
input which is handled by the main function.
'''

def main():
    testReadData()
    testOrganizeData()
    testSetDataType()
    testGetStationID()
    testStationInfo()
    testIsBikeAvailable()
    testIsDockAvailable()
    testBikeAvailableStations()
    testFullCapacityStations()
    testRentBike()
    testReturnBike()
    testGiveDirections()
    testRepeat()

main()
        
