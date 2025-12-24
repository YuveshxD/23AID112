#Program on calculating if the give integer is ODD or EVEN

#input
favouritenumber=int(input("Enter Your Favourite Number:"))
remainder=favouritenumber%2

#output
if remainder==0:
    print("Your Favourite Number is EVEN")
else:
    print("Your Favourite Number is ODD")