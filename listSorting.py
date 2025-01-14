cars = ['Bmw','Mercedez','Masarati','Audi','Defender','Tata']

print(cars)

#but above sort method actually Permanently changing the list.

#Then how we can use temporary?
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)
cars.reverse()
print(cars)

#len() function for finding the length of a list
#sorted() function for Alphabeticaly sort data Temporarly

print(len(cars))
