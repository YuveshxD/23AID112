#Using Loop To Print Different Condition on the list

list=[12,45,3,98,7,34,21]

#A) Print Each Number in the list
print("A) Print Each Number in the list:-")
for i in list:
    print(i)

#B) Print Only Numbers Greater Than 30
print("B) Print Only Numbers Greater Than 30")
for i in list:
    if i>30:
        print(i)

#C) Count How Many Numbers Are Greater Than 30
count=0
for i in list:
    if i>30:
        count+=1
print("Count of Numbers Greater Than 30:",count)
