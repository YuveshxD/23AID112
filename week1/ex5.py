#Program on Basic Operation

#Input
x=input("Enter Your First Number:")
y=input("Enter Your Second Number:")

#converting into integer
x1=int(x)
y1=int(y)

#Operations
sum=x1+y1
difference=x1-y1
product=x1*y1

#Output
print("The sum of the two numbers is:",sum)
print("The difference of the two numbers is:",difference)
print("The product of the two numbers is:",product)
if x1<y1:
    print("Your first number is less than your second number")
elif x1==y1:
    print("Both the numbers are same")
else:
    print("Your first number is greater than second number")

