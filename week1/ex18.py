#Program on Number Guessing Game

secret_number=7
user_guess=0

while user_guess !=secret_number:
    user_guess= int(input("Guess the Secret Number(0-50):"))
    if user_guess>secret_number:
        print("Too High")
    if user_guess<secret_number:
        print("Too Low")
print("Yes,You Guessed the Secret Number")
