## reyes_109739_project01_HareshQuizGame

## README:

### Haresh Quiz Game:
    
This project was created for institutional purposes. The project consists of creating a simple game using the **graphics.py** module.    
_Haresh Quiz Game_ is a quiz game that consists of 20 questions. You start with three lives, every time you answer a question     
incorrectly you lose one. If you lose all of your lives it's game over. If you reach the end without losing all of     
your lifes, you win.     
    
Like previously mentioned in this program we use the graphics.py module from Zelle's Book. The second module imported has two lists;  
one list holds all of the questions, while the other holds all of the answer, this way is easier to print them in the window since  
I can just call the list in a specific index, for an specific question. 
    
I used 10 functions, aside from the main. These are:  
    - **consoleLikeLook(win)**,   
    - **gameLogo(win)**,    
    - **instructions(win)**,   
    - **pressEnterWhenReady(win)**,  
    - **correctAnswer(win)**,   
    - **incorrectAnswer(win)**,   
    - **lifesExplanation(win)**,   
    - **game(win, questionList, answerList, availableLifes)**,   
    - **gameOver(win)**,    
    - **youWon(win)**  
 
 The functions *consoleLikeLook(win)*, *gameLogo(win)*, *instructions(win)* and *lifesExplanation(win)* are all functions that contain the  
 design of the game, basically the aesthetics. The *pressEnterWhenReady(win)* is a function that justs freezes the window until the  
 user enters any key, this function is used multiple times throughout the program. The functions *correctAnswer(win)* and  
 *incorrectAnswer(win)* display if you had a correct or incorrect answer. The *gameOver(win)* and *youWon(win)* functions display if you won  
 the game or if you lost. Finally, the *game(win, questionList, answerList, availableLifes)* function holds the algorithm that performs
 the game.

## CONTACT:

creator: **Jadnell H. Reyes Perez**
student_IdNum: **109739**
personal_email: **jadnell555@gmail.com**
institutional_email: **reyes_109739@students.pupr.edu**

