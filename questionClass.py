from graphics import *
from cheatSheet import *
from questionsTemplateFunction import *

class Question:

    def __init__(self, win, qNum, qSize):
        self.win = win
        self.qNum = qNum - 1
        self.qSize = qSize


    def makeQuestion(self, questionTitleList, questionsList):
        self.questionTitle = Text(Point(250, 100), questionTitleList[self.qNum])
        questionTitleTemplate(self.win, self.questionTitle)

        self.question = Text(Point(250, 150), questionsList[self.qNum])
        self.question.setSize(self.qSize)
        questionsTemplate(self.win, self.question)
        
        self.userAnswer = Entry(Point(250, 250), 10)
        self.userAnswer.setFill("green")
        self.userAnswer.draw(self.win)

        self.submit = Text(Point(250, 300), "Submit Answer")
        self.submit.setSize(16)
        self.submit.setStyle("bold italic")
        self.submit.setFace("helvetica")
        self.submit.setOutline("green")
        self.submit.draw(self.win)
        

        return self.questionTitle, self.question, self.userAnswer, self.submit


    
