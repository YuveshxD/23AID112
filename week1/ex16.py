#Program on printing only numbers that are divisible by 3 between 1-20

set=list(range(1,21))

for item in set:
    if item%3==0:
        print(item)

