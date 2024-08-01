import random

movies: list = ["Fast And Furiuos", "Spide-Man" ,"American sniper"]

movies.append("Jungle")

movies.insert(0 , "Joker")


print(f"The length of the movies list is : {len(movies)}")
print("movies list" , movies)



random_numbers: list = []
for i in range(10):
    random_numbers.append(random.randint(1,100))
print("random numbers list:", random_numbers)


random_bools: list = []
for i in range(10):
    random_bools.append(random.choice([True,False]))

    print("Random bolleans list:", random_bools)