#Program on determining user's age

#Input
age=int(input("Enter Your Age:"))

#Output
if age<13:
    print("You are a child")
elif 13<=age<=17:
    print("You are a Teenager")
elif 18<=age<=64:
    print("You are an adult")
else:
    print("You are a senior")
