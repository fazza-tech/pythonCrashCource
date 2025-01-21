magicians = ['tory','alana','abella','dani'] #created list

#creating loop 
for magician in magicians:
    print(f"Its an amazing bang {magician.title()}")
    print(f"I cant wait for your next perfomance {magician.title()} \n")

list_of_items = ['tomato','carrot','banana']

print("Your cart:")
for lists in list_of_items:
    print(f"\t {lists}") 

print("my fvrt pizzas:")

pizzas = ["angela","mia malkova","ablea"]

for piza in pizzas:
    print(f"my fvrt pizza is {piza}")

for value in range(1,11):
    print(value)

numbers = list(range(1,7))
print(numbers)

skip_nums=list(range(0,11,2))
print(skip_nums)

squares = []

for value in range(1,11):
    squares.append(value**2)

print(squares)

numbers = [1,2,3,4,5,6,7,8,9,0]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#List comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)



total = list(range(1,1000001))

print(min(total))
print(max(total))
print(sum(total))

odd = list(range(3,31,3))
print(odd)


cubes1 = []
for value in range(1,11):
    cubes1.append(value**3)
print(cubes1)

cubes = [value**3 for value in range(1,11)]
print(cubes)