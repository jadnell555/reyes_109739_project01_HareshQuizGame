from graphics import *
from cheatSheet import *  # File that contains questions and answers


def main():
    win = graphicWindow()                                 # Graphic Window
    consoleDesign(win)                                    # Retro console look
    gameLogo(win)                                         # Logo of the game at start
    instructions(win)                                     # Instructions of the game
    availableLifes = lifes(win)                           # List made from the lifes
    game(win, questionsList, answersList, availableLifes) # Quiz Game


def graphicWindow():
    win = GraphWin("Game", 500, 500)
    win.setBackground("green4")

    return win

def consoleDesign(win):

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

    pressKeyWhenReady(win)
    gameLogo.undraw()


def pressKeyWhenReady(win):

    pressKeyWhenReady = Text(Point(250, 425), "Press any key to continue!")
    pressKeyWhenReady.setSize(16)
    pressKeyWhenReady.setStyle("bold")
    pressKeyWhenReady.setFace("arial")
    pressKeyWhenReady.setFill("gray")
    pressKeyWhenReady.draw(win)

    for i in range(1):
        ready = win.getKey()

    pressKeyWhenReady.undraw()

def instructionsTemplate(win, ins_line):
    ins_line.setSize(14)
    ins_line.setStyle("italic")
    ins_line.setFace("helvetica")
    ins_line.setOutline("blue")
    ins_line.draw(win)
    

def instructions(win):
    questionTitle = Text(Point(250, 100), "Welcome to Haresh Quiz Game!")
    questionTitle.setSize(18)
    questionTitle.setStyle("bold italic")
    questionTitle.setFace("helvetica")
    questionTitle.setOutline("blue")
    questionTitle.draw(win)

    instructions = Text(Point(150, 150), "Instructions: ")
    instructions.setSize(16)
    instructions.setStyle("italic")
    instructions.setFace("helvetica")
    instructions.setOutline("blue")
    instructions.draw(win)

    ins_line1 = Text(Point(250, 175), "This game consists of 20 questions.")
    instructionsTemplate(win, ins_line1)

    ins_line2 = Text(Point(250, 200), "Each correct question earns you 1 point.")
    instructionsTemplate(win, ins_line2)

    ins_line3 = Text(Point(250, 225), "You have 3 lives. Everytime you answer")
    instructionsTemplate(win, ins_line3)

    ins_line4 = Text(Point(250, 250), "one question incorrectly you lose 1 life.")
    instructionsTemplate(win, ins_line4)

    ins_line5 = Text(Point(250, 275), "If you lose all of your lives it's game over.")
    instructionsTemplate(win, ins_line5)

    ins_line6 = Text(Point(250, 300), "The goal is to finish all questions.")
    instructionsTemplate(win, ins_line6)

    pressKeyWhenReady(win)

    questionTitle.undraw()
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

    pressKeyWhenReady(win)
    correct.undraw()


def incorrectAnswer(win):

    incorrect = Text(Point(250, 250), "YOU ARE INCORRECT! :|")
    incorrect.setFill("red")
    incorrect.setFace("helvetica")
    incorrect.setSize(24)
    incorrect.draw(win)

    pressKeyWhenReady(win)
    incorrect.undraw()

def lifesTemplate(win, life):
    
    life.setFill("red")
    life.setOutline("yellow")
    life.draw(win)

def lifesExpTemplate(win, life_exp):
    
    life_exp.setFace("helvetica")
    life_exp.setFill("red")
    life_exp.setStyle("bold")
    life_exp.setSize(20)
    life_exp.draw(win)

def lifes(win):
    # Life 1:
    life1 = Circle(Point(375, 75), 7)
    lifesTemplate(win, life1)

    # Life 2:
    life2 = Circle(Point(400, 75), 7)
    lifesTemplate(win, life2)

    # Life 3:
    life3 = Circle(Point(425, 75), 7)
    lifesTemplate(win, life3)

    # Lifes Explanation 
    life_exp1 = Text(Point(250, 225), "Those dots on the right upper")
    lifesExpTemplate(win, life_exp1)

    life_exp2 = Text(Point(250, 275), "corner are your lives.")
    lifesExpTemplate(win, life_exp2)

    life_exp3 = Text(Point(250, 325), "Good Luck!")
    lifesExpTemplate(win, life_exp3)

    pressKeyWhenReady(win)

    life_exp1.undraw()
    life_exp2.undraw()
    life_exp3.undraw()

    availableLifes = [life1, life2, life3]
    return availableLifes

def questionTitleTemplate(win, questionTitle):
    questionTitle.setSize(18)
    questionTitle.setStyle("bold italic")
    questionTitle.setFace("helvetica")
    questionTitle.setOutline("green")
    questionTitle.draw(win)

def questionsTemplate(win, question):
    question.setStyle("bold italic")
    question.setFace("helvetica")
    question.setOutline("green")
    question.draw(win)

def questionValidation(win, check, answersList, n, questionTitle, question, userAnswer, submit, correct, incorrect, availableLifes):
    if check == answersList[n]:
            questionTitle.undraw()
            question.undraw()
            userAnswer.undraw()
            submit.undraw()

            correctAnswer(win)

            correct = correct + 1

    else:
        if incorrect == 0:
            availableLifes[2].undraw()

        elif incorrect == 1:
            availableLifes[1].undraw()

        elif incorrect == 2:
            availableLifes[0].undraw()
            questionTitle.undraw()
            question.undraw()
            userAnswer.undraw()
            submit.undraw()
            gameOver(win)

        questionTitle.undraw()
        question.undraw()
        userAnswer.undraw()
        submit.undraw()

        incorrect = incorrect + 1
        incorrectAnswer(win)

def game(win, questionsList, answersList, availableLifes):
    questionCount = 0
    incorrect = 0
    correct = 0
    username = getUser(win)

    while questionCount != 11:

        # Question 1:
        questionCount = questionCount + 1

        questionTitle1 = Text(Point(250, 100), "Question #1")
        questionTitleTemplate(win, questionTitle1)

        question1 = Text(Point(250, 150), questionsList[0])
        question1.setSize(16)
        questionsTemplate(win, question1)

        userAnswer = Entry(Point(250, 250), 10)
        userAnswer.setFill("green")
        userAnswer.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)

        win.getMouse()

        check1 = userAnswer.getText()

        if check1 == answersList[0]:
            questionTitle1.undraw()
            question1.undraw()
            userAnswer.undraw()
            submit.undraw()

            correctAnswer(win)

            correct = correct + 1

        else:
            incorrect = incorrect + 1

            questionTitle1.undraw()
            question1.undraw()
            userAnswer.undraw()
            submit.undraw()
            availableLifes[2].undraw()

            incorrectAnswer(win)

        # Question 2:
        questionCount = questionCount + 1

        questionTitle2 = Text(Point(250, 100), "Question #2:")
        questionTitleTemplate(win, questionTitle2)

        question2 = Text(Point(250, 150), questionsList[1])
        question2.setSize(12)
        questionsTemplate(win, question2)

        userAnswer.setText("")
        userAnswer.draw(win)

        submit.draw(win)

        win.getMouse()

        check2 = userAnswer.getText()

        if check2 == answersList[1]:
            questionTitle2.undraw()
            question2.undraw()
            userAnswer.undraw()
            submit.undraw()

            correctAnswer(win)

            correct = correct + 1

        else:
            if incorrect == 0:
                availableLifes[2].undraw()
            elif incorrect == 1:
                availableLifes[1].undraw()

            incorrect = incorrect + 1

            questionTitle2.undraw()
            question2.undraw()
            userAnswer.undraw()
            submit.undraw()

            incorrectAnswer(win)

        # Question 3:
        questionCount = questionCount + 1

        questionTitle3 = Text(Point(250, 100), "Question #3:")
        questionTitleTemplate(win, questionTitle3)

        question3 = Text(Point(250, 150), questionsList[2])
        question3.setSize(16)
        questionsTemplate(win, question3)

        userAnswer.setText("")
        userAnswer.draw(win)

        submit.draw(win)

        win.getMouse()

        check3 = userAnswer.getText()
    
        questionValidation(win, check3, answersList, 2, questionTitle3, question3, userAnswer, submit, correct, incorrect, availableLifes)

        # Question 4:
        questionCount = questionCount + 1

        questionTitle4 = Text(Point(250, 100), "Question #4:")
        questionTitleTemplate(win, questionTitle4)

        question4 = Text(Point(250, 150), questionsList[3])
        question4.setSize(14)
        questionsTemplate(win, question4)

        userAnswer.setText("")
        userAnswer.draw(win)

        submit.draw(win)

        win.getMouse()

        check4 = userAnswer.getText()

        questionValidation(win, check4, answersList, 3, questionTitle4, question4, userAnswer, submit, correct, incorrect, availableLifes)

        # Question 5:
        questionCount = questionCount + 1

        questionTitle5 = Text(Point(250, 100), "Question #5:")
        questionTitleTemplate(win, questionTitle5)

        question5 = Text(Point(250, 150), questionsList[4])
        question5.setSize(16)
        questionsTemplate(win, question5)

        userAnswer.setText("")
        userAnswer.draw(win)

        submit.draw(win)

        win.getMouse()

        check5 = userAnswer.getText()

        questionValidation(win, check5, answersList, 4, questionTitle5, question5, userAnswer, submit, correct, incorrect, availableLifes)

        # Question 6:
        questionCount = questionCount + 1

        questionTitle6 = Text(Point(250, 100), "Question #6:")
        questionTitleTemplate(win, questionTitle6)

        question6 = Text(Point(250, 150), questionsList[5])
        question6.setSize(10)
        questionsTemplate(win, question6)

        userAnswer.setText("")
        userAnswer.draw(win)

        submit.draw(win)

        win.getMouse()

        check6 = userAnswer.getText()

        questionValidation(win, check6, answersList, 5, questionTitle6, question6, userAnswer, submit, correct, incorrect, availableLifes)

        # Question 7:
        questionCount = questionCount + 1

        questionTitle7 = Text(Point(250, 100), "Question #7:")
        questionTitleTemplate(win, questionTitle7)

        question7 = Text(Point(250, 150), questionsList[6])
        question7.setSize(12)
        questionsTemplate(win, question7)

        userAnswer.setText("")
        userAnswer.draw(win)

        submit.draw(win)

        win.getMouse()

        check7 = userAnswer.getText()

        questionValidation(win, check7, answersList, 6, questionTitle7, question7, userAnswer, submit, correct, incorrect, availableLifes)

        # Question 8:
        questionCount = questionCount + 1
        
        questionTitle8 = Text(Point(250, 100), "Question #8:")
        questionTitleTemplate(win, questionTitle8)

        question8 = Text(Point(250, 150), questionsList[7])
        question8.setSize(14)
        questionsTemplate(win, question8)

        userAnswer.setText("")
        userAnswer.draw(win)

        submit.draw(win)

        win.getMouse()

        check8 = userAnswer.getText()

        questionValidation(win, check8, answersList, 7, questionTitle8, question8, userAnswer, submit, correct, incorrect, availableLifes)

        # Question 9:
        questionCount = questionCount + 1

        questionTitle9 = Text(Point(250, 100), "Question #9:")
        questionTitleTemplate(win, questionTitle9)

        question9 = Text(Point(250, 150), questionsList[8])
        question9.setSize(10)
        questionsTemplate(win, question9)

        userAnswer.setText("")
        userAnswer.draw(win)

        submit.draw(win)

        win.getMouse()

        check9 = userAnswer.getText()

        questionValidation(win, check9, answersList, 8, questionTitle9, question9, userAnswer, submit, correct, incorrect, availableLifes)

        # Question 10:
        questionCount = questionCount + 1

        questionTitle10 = Text(Point(250, 100), "Question #10:")
        questionTitleTemplate(win, questionTitle10)

        question10 = Text(Point(250, 150), questionsList[9])
        question10.setSize(12)
        questionsTemplate(win, question10)

        userAnswer.setText("")
        userAnswer.draw(win)

        submit.draw(win)

        win.getMouse()

        check10 = userAnswer.getText()

        questionValidation(win, check10, answersList, 9, questionTitle10, question10, userAnswer, submit, correct, incorrect, availableLifes)

        youWon(win)
        totalCorrectAnswers(win, correct)
        thanksAndCreator(win)
        printScore(username, str(correct))

        break


def gameOver(win):

    gameOver = Text(Point(250, 250), "YOU LOST :/")
    gameOver.setFill("red")
    gameOver.setFace("helvetica")
    gameOver.setSize(24)
    gameOver.draw(win)

    pressKeyWhenReady(win)
    win.close()


def youWon(win):

    gameWon = Text(Point(250, 250), "YOU WON! (;")
    gameWon.setFill("yellow2")
    gameWon.setFace("helvetica")
    gameWon.setSize(24)
    gameWon.draw(win)

    pressKeyWhenReady(win)

    gameWon.undraw()

def correctAnsTemplate(win, correctAns):
    correctAns.setFill("blue")
    correctAns.setFace("helvetica")
    correctAns.setSize(20)
    correctAns.draw(win)

def totalCorrectAnswers(win, correct):

    correctAns1 = Text(Point(250, 250), "You had")
    correctAns2 = Text(Point(325, 250), correct)
    correctAns3 = Text(Point(250, 275), "correct answers.")

    correctAnsTemplate(win, correctAns1)
    correctAnsTemplate(win, correctAns2)
    correctAns2.setFill("green")
    correctAnsTemplate(win, correctAns3)

    pressKeyWhenReady(win)

    correctAns1.undraw()
    correctAns2.undraw()
    correctAns3.undraw()


def getUser(win):

    getUser = Text(Point(250, 100), "Enter your name:")
    getUser.setFace("helvetica")
    getUser.setFill("blue")
    getUser.setSize(20)
    getUser.draw(win)

    user = Entry(Point(250, 250), 15)
    user.setFill("blue")
    user.draw(win)

    submit = Text(Point(250, 300), "Submit Answer")
    submit.setSize(16)
    submit.setStyle("bold italic")
    submit.setFace("helvetica")
    submit.setOutline("blue")
    submit.setFill("blue")
    submit.draw(win)

    win.getMouse()
    submit.undraw()

    getUser.undraw()
    user.undraw()
    username = user.getText()
    return username


def printScore(user, correct):

    scoresFile = open("scores.txt", 'a+')
    scoresFile.write("\n" + "User:" + " \t " + "Score:" + "\n")
    scoresFile.write(user + " \t " + correct)
    scoresFile.close()


def thanksAndCreator(win):

    thanks = Text(Point(250, 150), "Thank you for playing!")
    thanks.setFill("blue")
    thanks.setSize(22)
    thanks.setFace("helvetica")
    thanks.draw(win)

    creator = Text(Point(250, 350), "Creator: Jadnell Reyes")
    creator.setFill("blue")
    creator.setSize(18)
    creator.setFace("helvetica")
    creator.draw(win)
    pressKeyWhenReady(win)
    win.close()


main()
