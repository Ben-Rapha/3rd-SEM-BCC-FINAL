from random import randint

def getFile():
    #TRY TO OPEN A WORD FILE IN THE SAME FOLDER AS THE HUNGAMAN PROGRAM, IF IT
    #EXIST WE USE THE WORD FILE AUTOMATICALY
    try:
        with open("wordlist.txt", "r"): infileName = "wordlist.txt"
            
    except IOError:
        foundFile = False
        #IF WORDLIST CAN'T BE FOUND, THEN WE ASK OUR USER TO CHOOSE A TEXT FILE
        infileName = input("Please choose a text file containing list of words: ")
        while not (foundFile):
            try:
                with open(infileName, "r"):foundFile = True
                    
            except IOError:
                infileName = input("\n Oops!!{0} file wasn't found!!\n\ nPlease try again, specify a specific path where the file can be found")
    return infileName

#CHOOSE A WORD RANDOMLY 
def chooseWord(infileName):
    infile = open(infileName, 'r')
    wordList = infile.readlines()
    totalWords = len(wordList)
    randomNum = randint(0, totalWords - 1)
    chosenWord = wordList[randomNum].replace('\n','')
    wordLen = len(chosenWord)
    return chosenWord, wordLen
