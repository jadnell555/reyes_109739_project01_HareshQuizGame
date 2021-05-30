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
