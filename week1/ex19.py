#Program on counting how many students got different grades

grades=[85, 92, 78, 65, 88, 91, 73, 89, 55, 94]

countA=0
countB=0
countC=0
count_below_70=0

for item in grades:
    if item>=90:
        countA+=1
    elif 89>=item>=80:
        countB+=1
    elif 79>=item>=70:
        countC+=1
    else:
        count_below_70+=1

print("Total Students with A Grade:",countA)
print("Total Students with B Grade:",countB)
print("Total Students with C Grade:",countC)
print("Total Students got below 70:",count_below_70)