age = int(input("What is your age?"))
if (age < 13):
    print("you are a Child")
elif(13 <= age < 18):
    print("you are a Teenager")
elif(18 <= age < 65):
    print("you are an Adult")
else:
    print("you are a Senior")

Score = int(input("What is your score /100"))
if  (Score >= 80):
    print("Your Score is an A")
elif  (Score >= 70):
    print("Your Score is a B")
elif  (Score >= 60):
    print("Your Score is a C")
elif  (Score >= 50):
    print("Your Score is a D")
elif  (Score >= 40):
    print("Your Score is a F")
else:
    print("Your Score is a U")
