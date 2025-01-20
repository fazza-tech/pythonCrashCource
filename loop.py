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
    square = value**2
    squares.append(square)

print(squares)