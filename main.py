favorite_animals = ['dag','cat','monkey','rabbit']
print(f"{favorite_animals}")
print(favorite_animals[1])
favorite_animals.remove('monkey')
print(f"{favorite_animals}")
favorite_animals.append('panda')
print(f"{favorite_animals}")
for favorite_animal in favorite_animals:
    print(f"I love {favorite_animal}") 


numbers=[5,4,3,2,1]
number_sum=0
for number in numbers:
    number_sum = number + number_sum
print(number_sum)