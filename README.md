## reyes_109739_project01_HareshQuizGame

## README:

### Haresh Quiz Game:
    
This project was created for institutional purposes. The project consists of  
creating a simple game using the **graphics.py** module. _Haresh Quiz Game_ is 
a quiz game that consists of 20 questions. You start with three lives, every  
time you answer a question incorrectly you lose one. If you lose all of your  
lives it's game over. If you reach the end without losing all of your lifes,  
you win. Like previously mentioned in this program we use the graphics.py module  
from Zelle's Book. The second module imported has two lists; one list holds all  
of the questions, while the other holds all of the answer, this way is easier to  
print them in the window since I can just call the list in a specific index, for  
an specific question. 
    
I used 10 functions, aside from the main. These are:  
    - **consoleDesign(win)**,   
    - **gameLogo(win)**,    
    - **instructions(win)**,   
    - **pressKeyWhenReady(win)**,  
    - **correctAnswer(win)**,   
    - **incorrectAnswer(win)**,   
    - **lifes(win)**,   
    - **game(win, questionList, answerList, availableLifes)**,   
    - **gameOver(win)**,    
    - **youWon(win)**,  
    - **totalCorrectAnswers(win, correct)**,  
    - **getUser(win)**,  
    - **printScore(user, correct)**,  
    - **thanksAndCreator(win)**    
 
The functions *consoleDesign(win)*, *gameLogo(win)*, *instructions(win)* and  
*lifes(win)* are all functions that contain the design of the game, basically  
the aesthetics. The *pressKeyWhenReady(win)* is a function that justs freezes  
the window until the user enters any key, this function is used multiple times  
throughout the program. The functions *correctAnswer(win)* and *incorrectAnswer(win)* 
display if you had a correct or incorrect answer. The *gameOver(win)* and  
*youWon(win)* functions display if you won the game or if you lost. The function  
*totalCorrectAnswers(win, correct)* displays how many correct answers you had  
if you win, while the *getUser(win)* function gets the name of the user that is  
playing. Both of these functions are needed for the *printScore(user, correct)*  
function that creates a .txt file that holds the user and his score. The  
*thanksAndCreator(win)* function just displays a thank you message and my name  
as the creator. Finally, the *game(win, questionList, answerList, availableLifes)* 
function holds the algorithm that performs the game.

## CONTACT:

creator: **Jadnell H. Reyes Perez**  
student_IdNum: **109739**  
personal_email: **jadnell555@gmail.com**  
institutional_email: **reyes_109739@students.pupr.edu**  

