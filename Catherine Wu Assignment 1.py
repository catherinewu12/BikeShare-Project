#assignment 1

'''
Assignment 1: Word Game
Name: Catherine Wu
Student ID: 20099368
Date created: September 27th, 2018
Date last modified: October 3rd, 2018

This program invites users to play five rounds of a word forming game.
The game provides two letters, one starting and one ending, and asks the player
to input a word which begins and ends with those letters, respectively.
The word is then validated against a list of words which has been cleansed
of any string longer than two letters, containing only identical letters (ex. 'aaa')
The player is scored based on the validity of their word, the length, and the letters they've used
'''

#load library needed for the program
import urllib.request 
import random

'''
Read the string of 10000 words and return them as a list
'''
def readWordList():
    response = urllib.request.urlopen("http://www.mit.edu/~ecprice/wordlist.10000")
    html = response.read()
    #converting to list of strings
    data = html.decode('utf-8').split()
    return data


'''
This functions goes through the list of 10000 words and removes all words longer than
two letters which are all identical letters (ex: 'aa', 'cccc', 'bb')
Once it has completed the removal of the invalid words, it returns a cleansed
version of the original list
'''

def listCleanser(wordList):

    listLength = len(wordList)
    wordIndex = 0

    #going through the list
    while wordIndex < listLength:
        
        #word is longer than one letter
        if len(wordList[wordIndex]) > 1:
            
            #if the number of times the first character [0] appears in the word
            #is the same as the length of the word (the whole word is the same letter)
            #remove the word from the list
            if wordList[wordIndex].count(wordList[wordIndex][0]) == len(wordList[wordIndex]):
                wordList.remove(wordList[wordIndex])

                #list length is one element shorter after removing a word
                listLength -= 1
                #after removing one word from the list, the index numbers of the words 
                #will be shifted backwards by one, thus we have to go back one index
                #number before moving onto the next word in the list
                wordIndex -= 1
            
        #move on to the next word         
        wordIndex += 1

    #return cleansed list   
    return wordList
            

'''
test the list cleansing function
wil not be called
'''
def testCleanser():
    #sample lists to test the cleanser function
    response = urllib.request.urlopen("http://www.cs.queensu.ca/home/cords2/shortList.txt")
    test = response.read()
    testData = test.decode('utf-8').split()

    list1 = ['a', 'aaa', 'abbb', 'bba']
    list2 = []
    list3 = ['dog', 'cat', 'a', 'aaa']

    #call the cleansing function and print the cleansed lists
    #compare with the initial lists to check for proper return of function
    print (listCleanser(testData))
    print (listCleanser(list1))
    print (listCleanser(list2))
    print (listCleanser(list3))


'''    
This function randomly produces two letters that will be given to the player and with
which they must make a word
'''
def generateLetters():
    
    #list the alphabet to generate the random letters
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    #random generation of letters
    firstLetter = random.randint(0, 25)
    lastLetter = random.randint(0, 25)
    return alphabet[firstLetter], alphabet[lastLetter]


'''
This function scores the answer that is given by the player.
playerAnswer is the response the player inputs for each round
letterStart and letterEnd are randomly generated letters which limit the
player's response and score
validWordList is the list of words which are being checked against the player's answer
Each letter has a specific number of points with bonus points for
longer words and same start/end letter
Points are taken away for entering a word not on the list or with the incorrect start/end letters
'''
def scoring(playerAnswer, letterStart, letterEnd, validWordList):

    #score per round begins at zero and is added to the total score 
    score = 0
        
    #points per letter
    letter_values = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 1, 'f': 5, 'g': 2, 'h': 3, 'i': 1, 'j': 9, 'k': 5,\
                     'l': 1, 'm': 2, 'n': 2, 'o': 1, 'p': 4, 'q': 15, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 8, 'w': 4, 'x': 15, 'y': 4, 'z': 15 } 

    #test validation of the word input by the player
    if playerAnswer[0].lower() == letterStart and playerAnswer[-1].lower() == letterEnd:
        if playerAnswer.lower() in validWordList:
            print ('You have entered a valid word!')

            #add the score for each letter, referring to scores in the
            #letter_values dictionary
            for letter in playerAnswer:
                score += letter_values[letter.lower()]

            #bonus points for long words!
            if len(playerAnswer) == 6:
                score += 3
            elif len(playerAnswer) == 7:
                score += 4
            elif len(playerAnswer) == 8:
                score += 5
            elif len(playerAnswer) > 8:
                score +=6

            if letterStart == letterEnd:
                score += 10

        #lose 10 points if the word is not found in the list        
        else:
            print ('That word is not valid. Sorry!')
            score -= 10

    #lose 2 points if the word does not star and end with the correct letter
    else:
        print ('That word does not contain the correct letters!')
        score -= 2

    #let player know how they are scoring
    print ('You have earned ' +str(score)+ ' points for this round!\n')

    #return the score for the round
    return score

'''
This function beings the game!
Calls the word list function, cleanser function, random letter generator function
Asks for user input
Sends these values to the scoring function to calculate the score per round
Adds the score from each round onto the total score and displays to the player after completion
of five rounds of the game
'''
def main():

    gameScore = 0
    rounds = 1

    #get data from the imported list of 10000 words and apply to the cleansing function
    originalList = readWordList()
    validWords = listCleanser(originalList)
    
    #five rounds
    while rounds < 6:
        print ('Round ' + str(rounds))
        
        #call to previous function to use the return values in starting the game
        letter1, letter2 = generateLetters()
            
        #ask the player for a word based on the game rules
        playerInput = input('Try to enter a word that starts with "' + letter1 + '" and ends with "' + letter2 + '": ')

        #add the score for each round into the player's total game score
        gameScore += scoring(playerInput, letter1, letter2, validWords)

        rounds += 1

    print ('Your final score is ' + str(gameScore) + '. Good game!')



#let's play!!!
main()


