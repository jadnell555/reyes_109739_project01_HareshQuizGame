from graphics import *


def main():
   # Graphic Window
    win = GraphWin("Game", 500, 500)
    win.setBackground("green4")

    answersList = [1, "blue", 25, "haresh", 3.14,
                   "python", "linus", 0, 20, 2.718]
    
    questionsList = ["How much is 2^0?", "What color was the font of the instructions?", "How much is 1/4 of 100?",
                     "What was the first word of the game's title?", "Which are the first 3 digits of PI?", 
                     "What programming language does Prof. Florez teach in CECS-3210?", "What is the first name of the creator of Linux?",
                     "What is the result of (1 + 2)(1^2 + 3(1) - 4)?", "What is the least amount of moves to solve a Rubik's Cube?", "Which are the first 4 digits of e (Euler's Constant)?"]

    consoleLikeLook(win)  # Retro console look
    gameLogo(win)         # Logo of the game at start
    instructions(win)     # Instructions of the game
    lifes(win)


    #correctAnswer(win)    # Correct answer
    #incorrectAnswer(win)  # Incorrect answer

    


    # Loop to find a specific coordinate
    # for i in range(1):
    #    p = win.getMouse()
    #    i = p
    #    print(i)

    for i in range(1):
        p = win.getMouse()

    win.close()  # close window


def consoleLikeLook(win):
    # Screen
    screen = Rectangle(Point(50, 50), Point(450, 450))
    screen.setFill("light gray")
    screen.draw(win)

    # Select button and Label
    selectButton = Rectangle(Point(78, 480), Point(121, 460))
    selectButton.setFill("pink")
    selectButton.draw(win)

    selectLabel = Text(Point(100, 471.0), "Select")
    selectLabel.setSize(8)
    selectLabel.setFace("courier")
    selectLabel.setStyle("bold")
    selectLabel.draw(win)

    # Power button and label
    powerButton = Rectangle(Point(380, 480), Point(420, 460))
    powerButton.setFill("pink")
    powerButton.draw(win)

    powerLabel = Text(Point(400, 471.0), "Power")
    powerLabel.setSize(8)
    powerLabel.setFace("courier")
    powerLabel.setStyle("bold")
    powerLabel.draw(win)

    # Console Logo
    consoleLogo = Text(Point(250, 471.0), "JH-BOY")
    consoleLogo.setSize(20)
    consoleLogo.setStyle("bold italic")
    consoleLogo.setFace("courier")
    consoleLogo.setTextColor("pink")
    consoleLogo.draw(win)


def gameLogo(win):
    gameLogo = Text(Point(250, 250), "Haresh Quiz Game")
    gameLogo.setSize(26)
    gameLogo.setStyle("bold italic")
    gameLogo.setFace("helvetica")
    gameLogo.setTextColor("blue3")
    gameLogo.draw(win)
    pressEnterWhenReady(win)
    gameLogo.undraw()


def pressEnterWhenReady(win):
    clickKeyWhenReady = Text(Point(250, 425), "Press any key to continue!")
    clickKeyWhenReady.setSize(16)
    clickKeyWhenReady.setStyle("bold")
    clickKeyWhenReady.setFace("arial")
    clickKeyWhenReady.setFill("gray")
    clickKeyWhenReady.draw(win)
    for i in range(1):
        ready = win.getKey()
    clickKeyWhenReady.undraw()


def instructions(win):
    intro = Text(Point(250, 100), "Welcome to Haresh Quiz Game!")
    intro.setSize(18)
    intro.setStyle("bold italic")
    intro.setFace("helvetica")
    intro.setOutline("blue")
    intro.draw(win)

    instructions = Text(Point(150, 150), "Instructions: ")
    instructions.setSize(16)
    instructions.setStyle("italic")
    instructions.setFace("helvetica")
    instructions.setOutline("blue")
    instructions.draw(win)

    ins_line1 = Text(Point(250, 175), "This game consists of 20 questions.")
    ins_line1.setSize(14)
    ins_line1.setStyle("italic")
    ins_line1.setFace("helvetica")
    ins_line1.setOutline("red")
    ins_line1.setOutline("blue")
    ins_line1.draw(win)

    ins_line2 = Text(
        Point(250, 200), "Each correct question earns you 1 point.")
    ins_line2.setSize(14)
    ins_line2.setStyle("italic")
    ins_line2.setFace("helvetica")
    ins_line2.setOutline("blue")
    ins_line2.draw(win)

    ins_line3 = Text(Point(250, 225), "You have 3 lives. Everytime you answer")
    ins_line3.setSize(14)
    ins_line3.setStyle("italic")
    ins_line3.setFace("helvetica")
    ins_line3.setOutline("blue")
    ins_line3.draw(win)

    ins_line4 = Text(
        Point(250, 250), "one question incorrectly you lose 1 life.")
    ins_line4.setSize(14)
    ins_line4.setStyle("italic")
    ins_line4.setFace("helvetica")
    ins_line4.setOutline("blue")
    ins_line4.draw(win)

    ins_line5 = Text(
        Point(250, 275), "If you lose all of your lives it's game over.")
    ins_line5.setSize(14)
    ins_line5.setStyle("italic")
    ins_line5.setFace("helvetica")
    ins_line5.setOutline("blue")
    ins_line5.draw(win)

    ins_line6 = Text(Point(250, 300), "The goal is to finish all questions.")
    ins_line6.setSize(14)
    ins_line6.setStyle("italic")
    ins_line6.setFace("helvetica")
    ins_line6.setOutline("blue")
    ins_line6.draw(win)

    pressEnterWhenReady(win)
    intro.undraw()
    instructions.undraw()
    ins_line1.undraw()
    ins_line2.undraw()
    ins_line3.undraw()
    ins_line4.undraw()
    ins_line5.undraw()
    ins_line6.undraw()

def correctAnswer(win):
    correct = Text(Point(250, 250), "YOU ARE CORRECT! :)")
    correct.setFill("gold3")
    correct.setFace("helvetica")
    correct.setSize(26)
    correct.draw(win)
    pressEnterWhenReady(win)
    correct.undraw()

def incorrectAnswer(win):
    incorrect = Text(Point(250, 250), "YOU ARE INCORRECT! :|")
    incorrect.setFill("red")
    incorrect.setFace("helvetica")
    incorrect.setSize(24)
    incorrect.draw(win)
    pressEnterWhenReady(win)
    incorrect.undraw()

def lifes(win):
    life1 = Circle(Point(375, 75), 7)
    life1.setFill("red")
    life1.setOutline("yellow")
    life1.draw(win)
    
    life2 = Circle(Point(400, 75), 7)
    life2.setFill("red")
    life2.setOutline("yellow")
    life2.draw(win)

    life3 = Circle(Point(425, 75), 7)
    life3.setFill("red")
    life3.setOutline("Yellow")
    life3.draw(win)

    life_exp1 = Text(Point(250, 225), "Those dots on the right upper")
    life_exp1.setFace("helvetica")
    life_exp1.setFill("red")
    life_exp1.setStyle("bold")
    life_exp1.setSize(20)
    life_exp1.draw(win)

    life_exp2 = Text(Point(250, 275), "corner are your lives.")
    life_exp2.setFace("helvetica")
    life_exp2.setFill("red")
    life_exp2.setStyle("bold")
    life_exp2.setSize(20)
    life_exp2.draw(win)
    
    life_exp3 = Text(Point(250, 325), "Good Luck!")
    life_exp3.setFace("helvetica")
    life_exp3.setFill("red")
    life_exp3.setStyle("bold")
    life_exp3.setSize(20)
    life_exp3.draw(win)
    pressEnterWhenReady(win)
    life_exp1.undraw()
    life_exp2.undraw()
    life_exp3.undraw()


main()
