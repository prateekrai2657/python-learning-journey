#membership operator is used to test whether a value variable is found in a sequence (string,list,tuple,set or dictionaries )
# 1.in
# 2.not in
# word ="APPLE"

# letter=input("Guess a letter in the secret word:")

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")

grades = {
    "sandy":"A",
    "bafila":"C",
    "prateek":"A+",
    "sameer":"F",
}

student =input("Enter the name of student: ")
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")