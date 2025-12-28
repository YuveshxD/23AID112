#Program on printing users fav movies in order

movies=[]

#Input
for i in range(5):
    favourites=input(f"Enter Your Favourite Movie #{i+1}:")
    movies.append(favourites)

#Priting The UserInput in List Format   
print("Your Favourite Movies Are:-")
count=1
for item in movies:
    print(count,".",item)
    count+=1