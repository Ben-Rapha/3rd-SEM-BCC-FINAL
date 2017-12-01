from random import randint
from cs1graphics import *

#CREATES A GUESS BUTTON HANDLER TO GRAB LETTERS       
class GuessButtonHandler(EventHandler):
        def __init__(self,entry,word,gridinput,gamewon,guessButton,Message4):
            self._textBox = entry
            self._Word = word
            self._guessLetters = []
            self._strikes = 0
            self._gridInput = gridinput
            self._gamewon = gamewon
            self._gamewon = False
            self._message4 = Message4
            self._guessButton = guessButton
            EventHandler.__init__(self)
            
        #FOR EVENT HANDLING  
        def handle(self,event):
            if event.getDescription() == "mouse click":
                grabM = self._textBox.getMessage().lower()
                self._textBox.setMessage("")
                if grabM == "" or grabM == " " or len(grabM) != 1:                                        
                    if len(grabM) != 1:                                                                   
                        message11.setMessage("Please only guess a single letter at a time. Try again!")
                        
                # IF THE GUESS LETTER IS IN THE WORD, AND IT HASN'T BEEN GUESSED YET BY THE PLAYER, THEN WE UPDATE OUR
                # GRID BY PLACING THE LETTER IN THE APPROPRIATE EMPTY SPACES ON THE GRID             
                if grabM in self._Word.lower() and not (grabM in self._guessLetters):
                    self._guessLetters.append(grabM)
                    print(self._guessLetters)
                    grid = self._Word

                    for letter in self._Word:
                        if (not(letter.lower() in self._Word) or not (letter.lower() in self._guessLetters)) and letter != " ":
                            grid = grid.replace(letter, " __ ")
                        self._gridInput.setMessage(grid)

                    if grid == self._Word:
                        self._gamewon == True
                        message11.setMessage("Congrats!!! You've guessed the word correctly.")
                        message11.move(7,90)
                        message11.setFontColor("forestgreen")
                        message11.setFontSize(25)
                        self._gridInput.setFontColor("forestgreen")
                        self._gridInput.setFontSize(30)
                        self._gridInput.setMessage(self._Word.upper())
                        Face()
                        paper.remove(self._textBox)
                        paper.remove(self._guessButton)
                        paper.remove(self._message4)
                        
                    else:
                        message11.setMessage(" Nice! {0} is in the word. Try another letter.".format(grabM.upper()))
                
                elif grabM in self._guessLetters:
                        message11.setMessage("You have already guessed {0}. Try anothe letter.".format(grabM.upper()))
                     
                else:
                    #WRONG GUESS ! ADD A STRIKE AND DRAW A PIECE OF THE HANGMAN
                    self._guessLetters.append(grabM)
                    message11.setMessage(" {0} is a wrong guess! Try another letter. ".format(grabM.upper()))
                    self._strikes = self._strikes + 1
                    drawPiece(self._strikes)
                    (self._strikes)
                    if self._strikes == 7:
                        message11.setMessage("Sorry! You didn't completely guess the word.")
                        message11.setFontColor("red")
                        message11.setFontSize(25)
                        self._gridInput.setFontSize(30)
                        self._gridInput.setFontColor("red")
                        self._gridInput.setMessage(self._Word.upper())
                        paper.remove(self._textBox)
                        paper.remove(self._guessButton)
                        paper.remove(self._message4)
                        
#EXIST HANDLER FOR EXITING THE GAME                       
class ExitButtonHandler(EventHandler):
        """ THIS IS A HANDLER CLASS FOR EXISTING THE PROGRAM"""
        def __init__(self,paper):
                self._paper = paper
                EventHandler.__init__(self)
                
        """ IF THE USER CLICKS ON THE CANVAS, THE PROGRAM IS TERMINATED"""
        def handle(self,event):
                if event.getDescription()== "mouse click":
                        self._paper.close()
                        exit()

#INFOMATION HANDLER FOR HANGMAN INSTRUCTIONAS
class infoButtonHandler(EventHandler):
    def __init__(self,paper,infoButton,infileName):
        self._paper = paper
        self._infoButton = infoButton
        self._infileName = infileName
        EventHandler.__init__(self)
    def handle(self,event):
        if event.getDescription() == "mouse click":
            self._paper = Canvas(800,300,)
            self._paper.setTitle("HUNGMAN INSTRUCTIONS")
            self._paper.setBackgroundColor("lightsalmon2")
            self._paper.add(helpM)
            M1 = Text("PRELUDE",15,Point(40,50))
            M2 = Text("A crowd begins to gather, they can't wait to see some real, justice. There's just one thing,",13,Point(290,70))
            M3 = Text("you aren't a real criminal, No! No!, you'r at the wrong place, at the wrong time.",13,Point(255,90))
            M4 = Text("you may think you're dead, but it's not like that at all,Yes, yes. You've a chance to live.",13,Point(275,110))
            M5 = Text("All you've gotta do is guess the right words and you can live to see another day.But don't get so yet,",13,Point(320,130))
            M6 = Text("If you make 7 wrong guess, YOU'RE TOAST!, GOODLUCK.",13,Point(197,150))
            M7 = Text("RULES",15,Point(29,180))
            M8 = Text("Choose one letter at a time, The secret word is nothing but ONLY ALPHABETS",14,Point(273,200))
            M9 = Text("If you wish to play again, just restart the program and a new secret word will be generated",14,Point(310,220))
            M10 = Text("Letters already guessesed will appear in the python shell. This to help you remember letters you already guessed.",14,Point(390,240))
            self._paper.add(M1)
            self._paper.add(M2)
            self._paper.add(M3)
            self._paper.add(M4)
            self._paper.add(M5)
            self._paper.add(M6)
            self._paper.add(M7)
            self._paper.add(M8)
            self._paper.add(M9)
            self._paper.add(M10)
#HAPPY FACE            
def Face():
       mainF = Circle(50,Point(100,60))
       mainF.setFillColor("papayawhip")
       paper.add(mainF)
       mouth = Circle(15,Point(115,80))
       mouth.setFillColor("black")
       paper.add(mouth)
       mouthCover = Rectangle(33,30,Point(115,70))
       mouthCover.setFillColor("papayawhip")
       mouthCover.setBorderColor("papayawhip")
       paper.add(mouthCover)
       eye1 = Circle(10,Point(100,55))
       eye1.setFillColor("white")
       eye2 = eye1.clone()
       eye2.move(40,0)
       paper.add(eye1)
       paper.add(eye2)
       eyeball1 = Circle(3,Point(107,60))
       eyeball1.setFillColor("black")
       paper.add(eyeball1)
       eyeball2 = eyeball1.clone()
       eyeball2.move(40,0)
       paper.add(eyeball2)

#STRIKES IF USER ENTERS WRONG GUESS       
def drawPiece(strike):
    if strike == 1:
        r1 = Rectangle(320,20,Point(480,590))
        r1.setBorderWidth(2)
        r1.setFillColor("tan3")
        paper.add(r1)
        r2 = Rectangle(20,350,Point(580,404))
        r2.setFillColor("tan2")
        r2.setBorderWidth(2)
        paper.add(r2)
        r3 = Rectangle(120,20,Point(530,220))
        r3.setFillColor("tan3")
        r3.setBorderWidth(2)
        paper.add(r3)
        r4 = Rectangle(60,20,Point(485,220))
        r4.setBorderWidth(2)
        r4.setFillColor("cornsilk")
        paper.add(r4)
        r5 = Rectangle(50,15,Point(500,237))
        r5.setFillColor("cornsilk")
        r5.setBorderWidth(2)
        paper.add(r5)
        c2 = Circle(6,Point(500,252))
        c2.setFillColor("cornsilk")
        c2.setBorderWidth(2)
        paper.add(c2)
        c3 = Circle(6,Point(500,265))
        c3.setFillColor("cornsilk")
        c3.setBorderWidth(2)
        paper.add(c3)
        a = Point(100,250)
        b = Point(120,270)
        p1 = Path(a,b)
        p1.move(470,200)
        paper.add(p1)
        p2 = Path(a,b)
        p2.move(470,50)
        paper.add(p2)
        
    elif strike == 2:
        hungHead= Circle(28,Point(500,299))
        hungHead.setBorderWidth(2)
        paper.add(hungHead)
        
    elif strike == 3:
        hungSpine = Rectangle(5,130,Point(500,391))
        hungSpine.setFillColor("black")
        paper.add(hungSpine)
        
    elif strike == 4:
        left1 = Point(100,150)
        left2 = Point(140,210)
        left3 = Point(140,215)
        left4 = Point(95,150)
        leftHand = Polygon(left1,left2,left3,left4)
        leftHand.move(406,195)
        leftHand.setFillColor("black")
        paper.add(leftHand)

    elif strike == 5:
        left1 = Point(100,150)
        left2 = Point(140,210)
        left3 = Point(140,215)
        left4 = Point(95,150)
        leftHand = Polygon(left1,left2,left3,left4)
        leftHand.move(406,195)
        leftHand.setFillColor("black")
        rightHand = leftHand.clone()
        rightHand.flip()
        rightHand.move(-13,0)
        paper.add(rightHand)
    
    elif strike == 6:
        leftLeg1 = Point(100,150)
        leftLeg2 = Point(123,210)
        leftLeg3 = Point(120,215)
        leftLeg4= Point(95,150)
        leftLeg= Polygon(leftLeg1,leftLeg2,leftLeg3,leftLeg4)
        leftLeg.move(407,307)
        leftLeg.setFillColor("black")
        paper.add(leftLeg)
    
    elif strike == 7:
        leftLeg1 = Point(100,150)
        leftLeg2 = Point(123,210)
        leftLeg3 = Point(120,215)
        leftLeg4= Point(95,150)
        leftLeg= Polygon(leftLeg1,leftLeg2,leftLeg3,leftLeg4)
        leftLeg.move(407,307)
        leftLeg.setFillColor("black")
        rightLeg = leftLeg.clone()
        rightLeg.flip()
        rightLeg.move(-14,0)
        paper.add(rightLeg)
        
        crossEye1 = Point(100,132)
        crossEye2 = Point(112,143)
        crossEye3 = Point(112,147)
        crossEye4 = Point(96,135)
        crossEye  = Polygon(crossEye1,crossEye2,crossEye3,crossEye4)
        crossEye.setFillColor("black")
        crossEye.move(408,153)
        paper.add(crossEye)

        #LEFTEYES
        crossEyeLeft = crossEye.clone()
        crossEyeLeft.flip()
        crossEyeLeft.move(13,0)
        paper.add(crossEyeLeft)
        
        #RIGHTEYES
        RightcrossEye = crossEye.clone()
        RightcrossEye.flip()
        RightcrossEye.move(-13,0)
        paper.add(RightcrossEye)
        
        #LEFTEYES
        RightcrossEyeLeft = RightcrossEye.clone()
        RightcrossEyeLeft.flip()
        RightcrossEyeLeft.move(-13,0)
        paper.add(RightcrossEyeLeft)

        #FaceMouth
        loseMouth = Rectangle(20,5,Point(500,310))
        loseMouth.setFillColor("black")
        paper.add(loseMouth)
        rightLeg = leftLeg.clone()
        rightLeg.flip()
        rightLeg.move(-14,0)
        paper.add(rightLeg)
        
#BACKGROUND OF THE GAME        
def backGround():
    ground1 = Circle(120,Point(100,600))
    ground1.setBorderColor("white")
    paper.add(ground1)
    #MEDIUM MOUNTAIN
    aa = Point(60,300)
    bb = Point(120,240)
    cc = Point(140,250)
    dd = Point(220,165)
    ee = Point(260,185)
    ff = Point(260,230)
    hh = Point(430,230)
    gg = Point(450,300)
    mount = Polygon(aa,bb,cc,dd,ee,ff,hh,gg)
    mount.setFillColor("wheat2")
    mount.move(257,276)
    paper.add(mount)
     #TIP ON THE MOUNTAIN 2
    topp = Point(334,200)
    topp1 = Point(369,160)
    topp2 = Point(410,200)
    topp3 = Point(390,180)
    topp4 = Point (370,200)
    topp5 = Point (350,185)
    topMan2 = Polygon(topp,topp1,topp2,topp3,topp4,topp5)
    topMan2.setFillColor("white")
    topMan2.move(114,270)
    #paper.add(topMan2)
    #Mountain BIG ONE
    a1 = Point(100,400)
    b1 = Point(180,368)
    c1 = Point(362,200)
    d1 = Point(432,400)
    mount2 = Polygon(a1,b1,c1,d1)
    mount2.setFillColor("wheat2")
    mount2.move(250,149.4)#240
    paper.add(mount2)
    #TIP ON THE MOUNTAIN
    top = Point(323,200)
    top1 = Point(389,140)
    top2 = Point(410,200)
    top3 = Point(390,180)
    top4 = Point (370,200)
    top5 = Point (350,185)
    topMan = Polygon(top,top1,top2,top3,top4,top5)
    topMan.setFillColor("white")
    topMan.move(223,210)
    paper.add(topMan)
   
    ground2 = Rectangle(800,400,Point(300,750))
    ground2.setBorderWidth(1)
    ground2.setBorderColor("white")
    ground2.setFillColor("darkolivegreen2")#darkolivegreen2 forestgreen green4 lightgreen limegreen palegreen4
    paper.add(ground2)
    return paper

paper = Canvas(700,700,)
message11 = Text("Let's play!!! Please Guess a letter",15,Point(350,50))
paper.add(message11)
helpM = Text("INSRUCTIONS ON HOW TO PLAY",15,Point(360,20))
