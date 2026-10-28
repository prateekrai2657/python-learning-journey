#Python quiz game 
questions =("how many elements are there in periodic table?:",
            "which animal lays the largest eggs?:",
            "which is the most abundant gas in earth's atmosphere?:",
            "how many bones are there in human body?:",
            "which planet is the hottest in the solar system?:",)
options = (
    ("A. 116", "B. 117", "C.118", "D.119"),
    ("A. whale", "B. crocodile", "C. ostrich", "D.elephant"),
    ("A. nitrogen", "B. carbon-dioxide", "C.hydrogen", "D.oxygen"),
    ("A. 206", "B. 207", "C.208", "D.209"),
    ("A. mercury", "B. venus", "C.earth", "D.mars")
)

answers = ("C","C","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question)
    for option in options[question_num]:
      print(option)
     
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess== answers[question_num]:
         score +=1
         print("correct!")
    else:
        print("incorrect!")
        print(f"{answers[question_num]} is the correct answer")  
    question_num +=1 
    
print("----------------------")
print("      RESULT      ")
print("----------------------")
    
print("anwers: ",end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(questions)*100)
print(f"your score is: {score}%")
