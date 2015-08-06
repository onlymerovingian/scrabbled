'''
Created on 6 Aug 2015

@author: william
'''

class wdict:
    #predefine a word list array
    word_list = []
    
    #constructor method
    def __init__(self):  
        with open('words.txt', 'r') as f:
            for line in f:
                self.word_list.append(line.rstrip())
                
        if not self.word_list:
            print("Error: Empty word list.")
            print("Did word.txt file parse correctly")
        
        
    #find matching words   
    #not a very optimised algorithm 
    def findWords(self, chars):
        matchedWords = []
        for i in range(len(self.word_list)):
            tmpBool = True
            for j in range(len(chars)):
                if not chars[j] in self.word_list[i]:
                    tmpBool = False
                    break
            if (tmpBool == True) & (len(self.word_list[i]) - 1 == len(chars)): 
                matchedWords.append(self.word_list[i])
        return matchedWords
