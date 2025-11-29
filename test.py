print("Math Test")
print("Write down either 1-4 as your answer for each question.")

score = 0

#Question 1
print("Q1) What is 6*6?")
print("1) 36")
print("2) 12")

answer = int(input("Write your answer here:  "))

if answer == 1 or answer == 36:
    score = score + 1
elif answer == 2 or answer == 12:
    score = score + 0
#Question 2
print("Q2) 2x + 12 = 4x - 4. What is x?")
print("1) x = 8")
print("2) x = 4")
print("3) x = 7")
print("4) x = 1")

answer_2 = int(input("Write your answer here:  "))

if answer_2 == 1 or answer_2 == 8:
    score = score + 1
elif answer_2 == 2 or answer_2 == 4:
    score = score + 0
elif answer_2 == 3 or answer_2 == 7:
    score = score + 0
elif answer_2 == 4 or answer_2 == 1:
    score = score + 0

#Question 3

print("Q3) What does sum mean?")
print("1) Something.")
print("2) The answer to an addition problem.")
print("3) Super Ultimate MoneyMaker.")

answer_3 = int(input("Write your answer here:  "))

if answer_3 == 1:
    score = score + 0
elif answer_3 == 2:
    score = score + 1
elif answer_3 == 3:
    score = score + 0

#Question 4

print("Q4) What is the largest 3 digit number?")
print("1) 100")
print("2) 999")
print("3) 555")
print("4) 1000")

answer_4 = int(input("Write your answer here:  "))

if answer_4 == 1 or answer_4 == 100:
    score = score + 0
elif answer_4 == 2 or answer_4 == 999:
    score = score + 1
elif answer_4 == 3 or answer_4 == 555:
    score = score + 0
elif answer_4 == 4 or answer_4 == 1000:
    score = score + 0

print("Score:", score)

Passing_or_No = int(input("What is your final score?  " ))

if score == 4:
    print("Excellent, you passed!")
if score == 3:
    print("Amazing, you passed!")
if score <= 2:
    print("You failed.")