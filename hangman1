from cs1graphics import*
from handlers import*
from getfile import*


##########################################################
#                                                        #
#                                                        #
#               hangman.py				 #	
#     ---------------------------------------------	 #
#							 #
#     Loads a random word from a list of allowed	 #
#     words, specified in an input file, and starts	 #
#     the game for you!					 #
#							 #
#     Author: KINGSLEY OTTO                              #
#							 #
#     cs1graphics.py library was used to generate the    #       
#     GUI for this program.                              #
#                                                        #
#                                                        #
#     HAVE FUN      ^__^                                 #
#                                                        #
##########################################################

#NOTE ALL THE WORDS YOU ENTER WILL APPEAR IN THE SHELL COLLECTIVELY 

def main(infileName,grabM):
    
    #CHOOSE WORD LIST FILE
    infileName = getFile()
    
    #CHOOSE A WORD AT RANDOM FROM THE WORDLIST
    Word,wordLen = chooseWord(infileName)
    
    #BACKGROUND/TITLE/BACKGROUDCOLOR
    paper = backGround()
    paper.setTitle("HANGMAN")
    paper.setBackgroundColor("azure2")

    #BUILD A GRID SPACE FOR EACH LETTER
    grid = "__"
    for i in range(wordLen-1):
        grid = (grid + " __")
    gridInput = Text(grid,20,Point(360,90))
    paper.add(gridInput)

    #ENTRY BOX WHERE LETTERS WILL BE ENTERED
    Entry = TextBox(60,35,Point(500,650))
    Entry.setMessage("")
    paper.add(Entry)

    #INFORMATION BUTTON FOR HANGMAN INSTRUCTIONS
    infoButton = Button("HELP",Point(50,650))
    infoButton.setFillColor("red")
    infoButton.setHeight(35)
    infoButton.setWidth(60)
    paper.add(infoButton)
    info = infoButtonHandler(infoButton,paper,infileName)
    infoButton.addHandler(info)
    
    #TYPE A LETTER MESSAGE
    Message4 = Text("Type a letter:",15,Point(390,650))
    paper.add(Message4)
    
    gamewon = False
    #GUESS BOX
    guessButton = Button("GUESS",Point(570,650))
    guessButton.setFillColor("steelblue3")
    guessButton.setHeight(35)
    guessButton.setWidth(60)
    paper.add(guessButton)
    gb = GuessButtonHandler(Entry,Word,gridInput,gamewon,guessButton,Message4)
    guessButton.addHandler(gb)
    
    #QUIT BUTTON
    quitButton = Button("  Quit  ",Point(650,20))
    quitButton.setFillColor("salmon")
    quitButton.addHandler(ExitButtonHandler(paper))
    paper.add(quitButton)
    
    gamewon = False
    return infileName,grabM
main(False,False)
    
