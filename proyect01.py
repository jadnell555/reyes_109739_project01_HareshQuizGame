from graphics import *


def main():
   # Graphic Window
    win = GraphWin("Game", 500, 500)
    win.setBackground("green4")

    consoleLikeLook(win)
    pressEnterWhenReady(win)

    gameIntro = Text(Point(250, 100), "This is the Haresh Quiz Game!")
    gameIntro.setSize(18)
    gameIntro.setStyle("bold italic")
    gameIntro.setFace("helvetica")
    gameIntro.setOutline("blue")
    gameIntro.draw(win)
    instructions(win)

    # Loop to find a specific coordinate
    # for i in range(1):
    #    p = win.getMouse()
    #    i = p
    #    print(i)

    for i in range(1):
        p = win.getMouse()

    win.close()  # close window
    pass


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


def pressEnterWhenReady(win):
    clickKeyWhenReady = Text(Point(250, 250), "When ready enter any key!")
    clickKeyWhenReady.setSize(18)
    clickKeyWhenReady.setStyle("bold")
    clickKeyWhenReady.setFace("arial")
    clickKeyWhenReady.draw(win)
    for i in range(1):
        ready = win.getKey()
    clickKeyWhenReady.undraw()

def instructions(win):
    instructions = Text(Point(150, 150), "Instructions: ")
    instructions.setSize(16)
    instructions.setStyle("italic")
    instructions.setFace("helvetica")
    instructions.setOutline("blue")
    instructions.draw(win)

    exp_line1 = Text(Point(250, 175), "This game consists of 20 questions.")
    exp_line1.setSize(14)
    exp_line1.setStyle("italic")
    exp_line1.setFace("helvetica")
    exp_line1.setOutline("red")
    exp_line1.setOutline("blue")
    exp_line1.draw(win)

    exp_line2 = Text(Point(250, 200), "Each correct question earns you 1 point.")
    exp_line2.setSize(14)
    exp_line2.setStyle("italic")
    exp_line2.setFace("helvetica")
    exp_line2.setOutline("blue")
    exp_line2.draw(win)

    exp_line3 = Text(Point(250, 225), "You have 3 lives. Everytime you anwer one")
    exp_line3.setSize(14)
    exp_line3.setStyle("italic")
    exp_line3.setFace("helvetica")
    exp_line3.setOutline("blue")
    exp_line3.draw(win)

    exp_line4 = Text(Point(250, 250), "question incorrectly you lose 1 life.")
    exp_line4.setSize(14)
    exp_line4.setStyle("italic")
    exp_line4.setFace("helvetica")
    exp_line4.setOutline("blue")
    exp_line4.draw(win)

    exp_line5 = Text(Point(250, 275), "The goal is to finish all questions.")
    exp_line5.setSize(14)
    exp_line5.setStyle("italic")
    exp_line5.setFace("helvetica")
    exp_line5.setOutline("blue")
    exp_line5.draw(win)
    
    





main()
