#Program on Temperature Converter adn Advice

#Input
celsius=int(input("Enter Temperature in Celsius Scale:"))

#Operation
fahrenheit=celsius*(9/5)+32

#Output
print("Temperature in fahrenheit scale:",fahrenheit)
if fahrenheit<32:                 
    print("Very cold! Wear thick jacket")
elif 32<=fahrenheit<=59:           
    print("Cold. Wear jacket")
elif 60<=fahrenheit<=77: 
    print("Nice weather")
else:
    print("Hot! Stay hydrated")
