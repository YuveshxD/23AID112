#Program for Determining exam results based on Score

#Input
score1=int(input("1st Exam Score(0-100):"))
score2=int(input("2nd Exam Score(0-100):"))

#Output
if score1>=50 and score2>=50:
    print("YOU PASSED!")
else:
    print("You need to retake some exams")