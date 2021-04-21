from graphics import *


def main():
   # Graphic Window
    win = GraphWin("Game", 500, 500)
    win.setBackground("green4")

    answersList = ["1", "blue", "25", "haresh", "3.14",
                   "python", "linus", "0", "20", "2.718"]

    questionsList = ["How much is 2^0?", "What color was the font of the instructions?", "How much is 1/4 of 100?",
                     "What was the first word of the game's title?", "Which are the first 3 digits of PI?",
                     "What programming language does Prof. Florez teach in CECS-3210?", "What is the first name of the creator of Linux?",
                     "What is the result of (1 + 2)(1^2 + 3(1) - 4)?", "What is the least amount of moves to solve a Rubik's Cube?", "Which are the first 4 digits of e (Euler's Constant)?"]

    consoleLikeLook(win)  # Retro console look
    gameLogo(win)         # Logo of the game at start
    instructions(win)     # Instructions of the game

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

    availableLifes = [life1, life2, life3]

    lifesExplanation(win)            # Lifes introduction
    game(win, questionsList, answersList,
         availableLifes)             # Game start

    # correctAnswer(win)    # Correct answer
    # incorrectAnswer(win)  # Incorrect answer

    # Loop to find a specific coordinate
    # for i in range(1):
    #    p = win.getMouse()
    #    i = p
    #    print(i)

    # for i in range(1):
    #    p = win.getMouse()

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


def lifesExplanation(win):

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
    return life_exp1


def game(win, questionsList, answersList, availableLifes):
    questionCount = 0
    incorrect = 0
    while questionCount != 10:

        # Question 1:
        questionCount = questionCount + 1
        questionTitle1 = Text(Point(250, 100), "Question #1:")
        questionTitle1.setSize(18)
        questionTitle1.setStyle("bold italic")
        questionTitle1.setFace("helvetica")
        questionTitle1.setOutline("green")
        questionTitle1.draw(win)

        question1 = Text(Point(250, 150), questionsList[0])
        question1.setSize(16)
        question1.setStyle("bold italic")
        question1.setFace("helvetica")
        question1.setOutline("green")
        question1.draw(win)

        userAnswer1 = Entry(Point(250, 250), 10)
        userAnswer1.setFill("green")
        userAnswer1.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)
        win.getMouse()

        check1 = userAnswer1.getText()
        if check1 == answersList[0]:
            questionTitle1.undraw()
            question1.undraw()
            userAnswer1.undraw()
            submit.undraw()
            correctAnswer(win)
            pressEnterWhenReady(win)
        else:
            incorrect = incorrect + 1
            questionTitle1.undraw()
            question1.undraw()
            userAnswer1.undraw()
            submit.undraw()
            availableLifes[2].undraw()
            incorrectAnswer(win)

        # Question 2:
        questionCount = questionCount + 1
        questionTitle2 = Text(Point(250, 100), "Question #2:")
        questionTitle2.setSize(18)
        questionTitle2.setStyle("bold italic")
        questionTitle2.setFace("helvetica")
        questionTitle2.setOutline("green")
        questionTitle2.draw(win)

        question2 = Text(Point(250, 150), questionsList[1])
        question2.setSize(12)
        question2.setStyle("bold italic")
        question2.setFace("helvetica")
        question2.setOutline("green")
        question2.draw(win)

        userAnswer2 = Entry(Point(250, 250), 10)
        userAnswer2.setFill("green")
        userAnswer2.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)
        win.getMouse()

        check2 = userAnswer2.getText()
        if check2 == answersList[1]:
            questionTitle2.undraw()
            question2.undraw()
            userAnswer2.undraw()
            submit.undraw()
            correctAnswer(win)
            pressEnterWhenReady(win)
        else:
            if incorrect == 0:
                availableLifes[2].undraw()
            elif incorrect == 1:
                availableLifes[1].undraw()
            incorrect = incorrect + 1
            questionTitle2.undraw()
            question2.undraw()
            userAnswer2.undraw()
            submit.undraw()
            incorrectAnswer(win)

        # Question 3:
        questionCount = questionCount + 1
        questionTitle3 = Text(Point(250, 100), "Question #3:")
        questionTitle3.setSize(18)
        questionTitle3.setStyle("bold italic")
        questionTitle3.setFace("helvetica")
        questionTitle3.setOutline("green")
        questionTitle3.draw(win)

        question3 = Text(Point(250, 150), questionsList[2])
        question3.setSize(16)
        question3.setStyle("bold italic")
        question3.setFace("helvetica")
        question3.setOutline("green")
        question3.draw(win)

        userAnswer3 = Entry(Point(250, 250), 10)
        userAnswer3.setFill("green")
        userAnswer3.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)
        win.getMouse()

        check3 = userAnswer3.getText()
        if check3 == answersList[2]:
            questionTitle3.undraw()
            question3.undraw()
            userAnswer3.undraw()
            submit.undraw()
            correctAnswer(win)
            pressEnterWhenReady(win)
        else:
            if incorrect == 0:
                availableLifes[2].undraw()
            elif incorrect == 1:
                availableLifes[1].undraw()
            elif incorrect == 2:
                availableLifes[0].undraw()
                questionTitle3.undraw()
                question3.undraw()
                userAnswer3.undraw()
                submit.undraw()
                gameOver(win)
                break
            questionTitle3.undraw()
            question3.undraw()
            userAnswer3.undraw()
            submit.undraw()
            incorrect = incorrect + 1
            incorrectAnswer(win)

        # Question 4:
        questionCount = questionCount + 1
        questionTitle4 = Text(Point(250, 100), "Question #4:")
        questionTitle4.setSize(18)
        questionTitle4.setStyle("bold italic")
        questionTitle4.setFace("helvetica")
        questionTitle4.setOutline("green")
        questionTitle4.draw(win)

        question4 = Text(Point(250, 150), questionsList[3])
        question4.setSize(16)
        question4.setStyle("bold italic")
        question4.setFace("helvetica")
        question4.setOutline("green")
        question4.draw(win)

        userAnswer4 = Entry(Point(250, 250), 10)
        userAnswer4.setFill("green")
        userAnswer4.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)
        win.getMouse()

        check4 = userAnswer4.getText()
        if check4 == answersList[3]:
            questionTitle4.undraw()
            question4.undraw()
            userAnswer4.undraw()
            submit.undraw()
            correctAnswer(win)
            pressEnterWhenReady(win)
        else:
            if incorrect == 0:
                availableLifes[2].undraw()
            elif incorrect == 1:
                availableLifes[1].undraw()
            elif incorrect == 2:
                availableLifes[0].undraw()
                questionTitle4.undraw()
                question4.undraw()
                userAnswer4.undraw()
                submit.undraw()
                incorrectAnswer(win)
                gameOver(win)
                break
            incorrect = incorrect + 1
            questionTitle4.undraw()
            question4.undraw()
            userAnswer4.undraw()
            submit.undraw()
            incorrectAnswer(win)

        # Question 5:
        questionCount = questionCount + 1
        questionTitle5 = Text(Point(250, 100), "Question #5:")
        questionTitle5.setSize(18)
        questionTitle5.setStyle("bold italic")
        questionTitle5.setFace("helvetica")
        questionTitle5.setOutline("green")
        questionTitle5.draw(win)

        question5 = Text(Point(250, 150), questionsList[4])
        question5.setSize(16)
        question5.setStyle("bold italic")
        question5.setFace("helvetica")
        question5.setOutline("green")
        question5.draw(win)

        userAnswer5 = Entry(Point(250, 250), 10)
        userAnswer5.setFill("green")
        userAnswer5.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)
        win.getMouse()

        check5 = userAnswer5.getText()
        if check5 == answersList[4]:
            questionTitle5.undraw()
            question5.undraw()
            userAnswer5.undraw()
            submit.undraw()
            correctAnswer(win)
            pressEnterWhenReady(win)
        else:
            if incorrect == 0:
                availableLifes[2].undraw()
            elif incorrect == 1:
                availableLifes[1].undraw()
            elif incorrect == 2:
                availableLifes[0].undraw()
                questionTitle5.undraw()
                question5.undraw()
                userAnswer5.undraw()
                submit.undraw()
                gameOver(win)
                break
            incorrect = incorrect + 1
            questionTitle5.undraw()
            question5.undraw()
            userAnswer5.undraw()
            submit.undraw()
            incorrectAnswer(win)

        # Question 6:
        questionCount = questionCount + 1
        questionTitle6 = Text(Point(250, 100), "Question #6:")
        questionTitle6.setSize(18)
        questionTitle6.setStyle("bold italic")
        questionTitle6.setFace("helvetica")
        questionTitle6.setOutline("green")
        questionTitle6.draw(win)

        question6 = Text(Point(250, 150), questionsList[5])
        question6.setSize(16)
        question6.setStyle("bold italic")
        question6.setFace("helvetica")
        question6.setOutline("green")
        question6.draw(win)

        userAnswer6 = Entry(Point(250, 250), 10)
        userAnswer6.setFill("green")
        userAnswer6.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)
        win.getMouse()

        check6 = userAnswer6.getText()
        if check6 == answersList[5]:
            questionTitle6.undraw()
            question6.undraw()
            userAnswer6.undraw()
            submit.undraw()
            correctAnswer(win)
            pressEnterWhenReady(win)
        else:
            if incorrect == 0:
                availableLifes[2].undraw()
            elif incorrect == 1:
                availableLifes[1].undraw()
            elif incorrect == 2:
                availableLifes[0].undraw()
                questionTitle6.undraw()
                question6.undraw()
                userAnswer6.undraw()
                submit.undraw()
                gameOver(win)
                break
            incorrect = incorrect + 1
            questionTitle6.undraw()
            question6.undraw()
            userAnswer6.undraw()
            submit.undraw()
            incorrectAnswer(win)

        # Question 7:
        questionCount = questionCount + 1
        questionTitle7 = Text(Point(250, 100), "Question #7:")
        questionTitle7.setSize(18)
        questionTitle7.setStyle("bold italic")
        questionTitle7.setFace("helvetica")
        questionTitle7.setOutline("green")
        questionTitle7.draw(win)

        question7 = Text(Point(250, 150), questionsList[6])
        question7.setSize(16)
        question7.setStyle("bold italic")
        question7.setFace("helvetica")
        question7.setOutline("green")
        question7.draw(win)

        userAnswer7 = Entry(Point(250, 250), 10)
        userAnswer7.setFill("green")
        userAnswer7.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)
        win.getMouse()

        check7 = userAnswer7.getText()
        if check7 == answersList[6]:
            questionTitle5.undraw()
            question7.undraw()
            userAnswer7.undraw()
            submit.undraw()
            correctAnswer(win)
            pressEnterWhenReady(win)
        else:
            if incorrect == 0:
                availableLifes[2].undraw()
            elif incorrect == 1:
                availableLifes[1].undraw()
            elif incorrect == 2:
                availableLifes[0].undraw()
                questionTitle7.undraw()
                question7.undraw()
                userAnswer7.undraw()
                submit.undraw()
                gameOver(win)
                break
            incorrect = incorrect + 1
            questionTitle7.undraw()
            question7.undraw()
            userAnswer7.undraw()
            submit.undraw()
            incorrectAnswer(win)

        # Question 8:
        questionCount = questionCount + 1
        questionTitle8 = Text(Point(250, 100), "Question #8:")
        questionTitle8.setSize(18)
        questionTitle8.setStyle("bold italic")
        questionTitle8.setFace("helvetica")
        questionTitle8.setOutline("green")
        questionTitle8.draw(win)

        question8 = Text(Point(250, 150), questionsList[7])
        question8.setSize(16)
        question8.setStyle("bold italic")
        question8.setFace("helvetica")
        question8.setOutline("green")
        question8.draw(win)

        userAnswer8 = Entry(Point(250, 250), 10)
        userAnswer8.setFill("green")
        userAnswer8.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)
        win.getMouse()

        check8 = userAnswer8.getText()
        if check8 == answersList[7]:
            questionTitle8.undraw()
            question8.undraw()
            userAnswer8.undraw()
            submit.undraw()
            correctAnswer(win)
            pressEnterWhenReady(win)
        else:
            if incorrect == 0:
                availableLifes[2].undraw()
            elif incorrect == 1:
                availableLifes[1].undraw()
            elif incorrect == 2:
                availableLifes[0].undraw()
                questionTitle8.undraw()
                question8.undraw()
                userAnswer8.undraw()
                submit.undraw()
                gameOver(win)
                break
            incorrect = incorrect + 1
            questionTitle8.undraw()
            question8.undraw()
            userAnswer8.undraw()
            submit.undraw()
            incorrectAnswer(win)

        # Question 9:
        questionCount = questionCount + 1
        questionTitle9 = Text(Point(250, 100), "Question #9:")
        questionTitle9.setSize(18)
        questionTitle9.setStyle("bold italic")
        questionTitle9.setFace("helvetica")
        questionTitle9.setOutline("green")
        questionTitle9.draw(win)

        question9 = Text(Point(250, 150), questionsList[8])
        question9.setSize(16)
        question9.setStyle("bold italic")
        question9.setFace("helvetica")
        question9.setOutline("green")
        question9.draw(win)

        userAnswer9 = Entry(Point(250, 250), 10)
        userAnswer9.setFill("green")
        userAnswer9.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)
        win.getMouse()

        check9 = userAnswer9.getText()
        if check9 == answersList[8]:
            questionTitle9.undraw()
            question9.undraw()
            userAnswer9.undraw()
            submit.undraw()
            correctAnswer(win)
            pressEnterWhenReady(win)
        else:
            if incorrect == 0:
                availableLifes[2].undraw()
            elif incorrect == 1:
                availableLifes[1].undraw()
            elif incorrect == 2:
                availableLifes[0].undraw()
                questionTitle9.undraw()
                question9.undraw()
                userAnswer9.undraw()
                submit.undraw()
                gameOver(win)
                break
            incorrect = incorrect + 1
            questionTitle9.undraw()
            question9.undraw()
            userAnswer9.undraw()
            submit.undraw()
            incorrectAnswer(win)

        # Question 10:
        questionCount = questionCount + 1
        questionTitle10 = Text(Point(250, 100), "Question #10:")
        questionTitle10.setSize(18)
        questionTitle10.setStyle("bold italic")
        questionTitle10.setFace("helvetica")
        questionTitle10.setOutline("green")
        questionTitle10.draw(win)

        question5 = Text(Point(250, 150), questionsList[9])
        question5.setSize(16)
        question5.setStyle("bold italic")
        question10.setFace("helvetica")
        question10.setOutline("green")
        question10.draw(win)

        userAnswer10 = Entry(Point(250, 250), 10)
        userAnswer10.setFill("green")
        userAnswer10.draw(win)

        submit = Text(Point(250, 300), "Submit Answer")
        submit.setSize(16)
        submit.setStyle("bold italic")
        submit.setFace("helvetica")
        submit.setOutline("green")
        submit.draw(win)
        win.getMouse()

        check10 = userAnswer10.getText()
        if check10 == answersList[9]:
            questionTitle5.undraw()
            question10.undraw()
            userAnswer10.undraw()
            submit.undraw()
            correctAnswer(win)
            pressEnterWhenReady(win)
        else:
            if incorrect == 0:
                availableLifes[2].undraw()
            elif incorrect == 1:
                availableLifes[1].undraw()
            elif incorrect == 2:
                availableLifes[0].undraw()
                questionTitle10.undraw()
                question10.undraw()
                userAnswer10.undraw()
                submit.undraw()
                gameOver(win)
                break
            incorrect = incorrect + 1
            questionTitle10.undraw()
            question10.undraw()
            userAnswer10.undraw()
            submit.undraw()
            incorrectAnswer(win)


def gameOver(win):
    gameOver = Text(Point(250, 250), "YOU LOST :/")
    gameOver.setFill("red")
    gameOver.setFace("helvetica")
    gameOver.setSize(24)
    gameOver.draw(win)
    pressEnterWhenReady(win)
    win.close()


main()
