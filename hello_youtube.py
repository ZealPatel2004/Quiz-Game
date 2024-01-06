#Today we will be building a basic quiz game in python
def new_game():
    guesses=[]
    correctGuesses=0
    question_num=1
    for key in questions:
        print("-----------------------------------------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("Enter A,B or C: ")
        guess=guess.upper()
        guesses.append(guess)
        correctGuesses+=check_answer(questions.get(key),guess)

        question_num+=1
    display_score(correctGuesses,guesses)
#----------------------
def check_answer(answer,guess):
    if answer==guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0

#----------------------
def display_score(correctguesses,guesses):
    print("--------------------------")
    print("RESULTS")
    print("-------------------------------")
    print("Answers: ",end="")
    for i in questions:
        print(questions.get(i),end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score=(correctguesses/len(questions))*100
    print("Your score is: "+str(score)+"%")





#----------------------
def play_again():
    response=input("Do you want to play again: Yes or no")
    response=response.upper()
    if(response=="YES"):
        return True
    else:
        return False

#----------------------


#lets now use dictonaries in python in order to create the questions.
#We can think of dictonaries as a set of keys and values

questions={"Who created the python language: ":"A",
           "What year was the python language created: ":"B",
           "Is the earth round: ":"C"}

#The questions are the key and the answer choices are the value.
options=[["A:Guido Van Rossum","B:Elon Musk","C:Joe Biden"],
         ["A:1989","B:1991","C:2014"],
         ["A:N/A","B:False","C:True"]]

new_game()
while play_again():
    new_game()

print("Quiz is over")