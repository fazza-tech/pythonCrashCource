
#create a list for bycicles
bicycles = ["trek","canndondale","redline","specialized"]
print(bicycles[0].title())

memory = f"My first cycle was a {bicycles[0].title()}."
print(memory)

names = ["Johna","Jesus","Muhammed","Moses"]
print(names)
pbuh = "Peace and Blessing Up On Him"
print(f"Assalamu Alaykum {names[2].upper()} {pbuh}.")


#Modifying lists

motorcycles = ["suzuki","honda","yamaha", "apprelia"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)
motorcycles.append("suzuki")
print(motorcycles)
motorcycles.insert(0,"apprelia")
del motorcycles[3]
popped_motor = motorcycles.pop()

popped_exp = motorcycles.pop(1)
msg = f"I sold the {popped_exp.title()} ,bcz its Expensive "
print(msg)

nxt_exp = "apprelia"
motorcycles.remove(nxt_exp)
print(motorcycles)
msg2 = f"I also sold {nxt_exp.title()} bcz its also expensive"
print(msg2)

numbers = []

numbers.append("9895998571")
numbers.append("79022246337")

members = ["Malavika","Akshara","Black"]
msg1 = f"Hi {members[0]}, please come and eat my cake😁"
print(msg1)

members.insert(0, 'angel')
print(members[0].title())

unfriend = members.pop(2)
print(members)
print(f"{unfriend} she is unfriended.")

