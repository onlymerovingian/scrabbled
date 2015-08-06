'''
Created on 6 Aug 2015

@author: william
'''
import argparse

from dict import wdict

#verify input arguments, return verified args
def verifyChars(chars):
    verifiedChars = []
    for i in range(len(chars)):
        if (len(chars[i]) == 1):
            verifiedChars.append(chars[i])
        else:
            print('Nope')
    return verifiedChars

#parses arguments from command line
def getChars():
    parser = argparse.ArgumentParser(description='Generate Scrabble Words')
    parser.add_argument('chars', type=str, nargs='+')
    array = parser.parse_args()
    
    #does the array exist, if not exit
    if not array:
        print("Parsing Error occurred")
        exit(1)
        
    array.chars = verifyChars(array.chars)
    
    return array.chars
chars = getChars()

dictionary = wdict()
print dictionary.findWords(chars)


