questions = ("How many elements are in the periodic table?: ",
            "Which animal lays the largest eggs?: ",
            "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet in the solar system is the hottest?: ")
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostritch"),
           ("A. Nitrogen", "B. Oxygen", "C. Hydrogen", "D. Carbon Dioxide"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0 
question_num = 0


for question in questions:
    print(3*"--------------------")
    print(question)
    for option in options[question_num]:
        print(option) 
    guess = (input("Enter (A, B, C, D): ")).upper()
    print()
    guesses.append(guess)
    if guess == answers[question_num]:
            score += 1
            print("Correct")
    else:
            print("*Wrong*")
            print(f"{answers[question_num]} is the Correct Answer")
    question_num += 1


print(2*"---------------",end="")
print("Results", end="")
print(2*"---------------")

print("Guesses: ", end="")
for guess in guesses:
      print(guess, end=" ")
print()

print("Answers: ", end="")
for answer in answers:
      print(answer, end=" ")
print()

score = float((score / len(questions)) * 100)
print(f"Your score is: {round(score,2)}%")
