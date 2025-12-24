#Program on Traffic Simulator

#Input
signal_color=input("Enter the color of the Traffic Signal:").lower()

#Output
if signal_color=="red":
    print("STOP!")
elif signal_color=="yellow":
    print("Slow Down and Prepare to Stop")
elif signal_color=="green":
    print("You can GO!")
else:
    print("Wrong Input!")