## reyes_109739_project01_HareshQuizGame

## README:

### Haresh Quiz Game:
    
This project was created for institutional purposes. The project consists of creating a simple game using the **graphics.py** module. _Haresh Quiz Game_ is a quiz game that consists of 20 questions. You start with three lives, every time you answer a question incorrectly you lose one. If you lose all of your lives it's game over. If you reach the end without losing all of your lifes, you win. Like previously mentioned in this program we use the graphics.py module from Zelle's Book. The second module imported has two lists; one list holds all of the questions, while the other holds all of the answer, this way is easier to print them in the window since I can just call the list in a specific index, for an specific question.

This branch titled **project01_B** contains the second version of HareshQuizGame. The objective of part B was to implement the same game using functions and modularization. 
    
In version A of the game I used 10 functions, aside from the main. These were:  
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
 
The functions _**consoleDesign(win)**_, _**gameLogo(win)**_, _**instructions(win)**_ and _**lifes(win)**_ are all functions that contain the design of the game, basically the aesthetics. The _**pressKeyWhenReady(win)**_ is a function that justs freezes the window until the user enters any key, this function is used multiple times throughout the program. The functions _**correctAnswer(win)**_ and _**incorrectAnswer(win)**_ display if you had a correct or incorrect answer. The _**gameOver(win)**_ and _**youWon(win)**_ functions display if you won the game or if you lost. The function _**totalCorrectAnswers(win, correct)**_ displays how many correct answers you had if you win, while the _**getUser(win)**_ function gets the name of the user that is playing. Both of these functions are needed for the _**printScore(user, correct)**_ function that creates a .txt file that holds the user and his score. The _**thanksAndCreator(win)**_ function just displays a thank you message and my name as the creator. Finally, the _**game(win, questionList, answerList, availableLifes)**_ function holds the algorithm that performs the game.

Aside from the already mentioned functions, I added a few more to reduce code repetition, and enhance the program's modularity. The added functions were:
- **instructionsTemplate(win, ins_line)**, which is used as a template for the intructions
- **lifesTemplate(win, life_exp)**, which is used as a template as well, for the lifes
- **lifesExpTemplate(win, life_exp)**, which is used as a template for the explanation of how the lifes work
- **questionsTitleTemplate(win, questionTitle)**, which is used as a template for the question Titles
- **questionTemplate(win, question)**, which is used as a template for the questions
- **questionValidation(win, check, answerList, n, questionTitle, question, userAnswer, submit, correct, incorrect, availableLifes)**, which contains the validation of the questions to know when to remove lifes. 
- **correctAnsTemplate(win, correctAns)**, which is used as a template for the total correct answers window.

As we can see all of these functions were implemented to reduce code repetition. While most of them have the title template, making it easier to recognize, the questionValidation() function isn't actually a template so it doesn't have the word in it's name. This implementation reduced the code from 986 lines of code to 631 lines, making the program simpler and more manageable.

## CONTACT:

creator: **Jadnell H. Reyes Perez**  
student_IdNum: **109739**  
personal_email: **jadnell555@gmail.com**  
institutional_email: **reyes_109739@students.pupr.edu**  

