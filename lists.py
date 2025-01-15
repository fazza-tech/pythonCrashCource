
motorcycles = ['bmw', 'KTM', 'ducati']
print(motorcycles)

motorcycles.append('RE') #one argument
print(motorcycles)
poped_bike = motorcycles.pop()#end of the list
print(poped_bike)
msg = f"im last owned bike is {poped_bike}"
print(msg)

first_bike = motorcycles.pop(0).title()
print(first_bike)
msg1 = f"My first bike was a  {first_bike.title()}"
print(msg1)

too_expensive = ('ducati')
motorcycles.remove(too_expensive)
print(type(too_expensive))
msg2 = f"{too_expensive.title()} very expensive"
print(msg2)
print(motorcycles)
motorcycles.insert(0,'Access 125')
print(motorcycles)

#len() , sorted() , .sort, .reverse

cars = ['bmw', 'subaru','masarati', 'mercedes']

print(len(cars)-1)

print(sorted(cars))
print(cars)
cars.sort()
print(cars)

cars.reverse()
print(cars)

