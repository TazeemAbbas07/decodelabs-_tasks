points=0

print("Welcome to quiz game")
print("Answer The Following Questions")

answer=input("Q1-- What is Capital Of France: ")

if answer.strip().lower()=="paris":
    points+=1
    print("--Correct--")
else:
    print("Wrong answer")

answer=input("Q2-- How many days are there in a week: ")
if answer.strip()=="7":
    points+=1
    print("--Correct--")
else:
    print("Wrong answer")

answer=input("Q3-- Which is Largest Continent of World: ")
if answer.strip().lower()=="asia":
    points+=1
    print("--Correct--")
else:
    print("Wrong answer")

print("QUIZ COMPLETED")
print("Your Final Score is : ",points,"/3")
