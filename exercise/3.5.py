
members = ['akshara','vrindha','stelna']
print(f"{members[0]} can't cum anymore guyzzzz.")
del members[0]
members.insert(0,"Teena")
print(members)

print(f"Hey {members[0]},{members[1]},{members[2]}.... I can't wait for u anymore guyzz... Please come and eat my cake💘")

print(f"hey guyz..i found that we got a big pool here...im going to add more...")
#Use insert() to add one new guest to the beginning of your list.
members.insert(0,'Mia ')
print(members)

#Use insert() to add one new guest to the middle of your list.
members.insert(2,'Gabbie ')
print(members)

#Use append() to add one new guest to the end of your list.
members.append(' Ames')
print(members)

#Print a new set of invitation messages, one for each person in your list.
print(f"Hi {members[0]}, Please come to my Party🎉💃")
print(f"Hi {members[1]}, Please come to my Party🎉💃")
print(f"Hi {members[2]}, Please come to my Party🎉💃")
print(f"Hi {members[3]}, Please come to my Party🎉💃")
print(f"Hi {members[4]}, Please come to my Party🎉💃")
print(f"Hi {members[5]}, Please come to my Party🎉💃")

#Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

#Add a new line that prints a message saying that you can invite only three people for dinner.
print(f"Sorry guyz... I can only invite 3 people for my dinner🥲")


#Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
teena = members.pop(1)
print(f"Sorry {teena} chechi, I miss u alot.")
print(members)
vrindha = members.pop(2)
print(f"Sorry {vrindha}, I miss u.")
print(members)
stelna = members.pop(2)
print(f"Im sorry {stelna}, I m gonna miss u a lot.")
print(members)

#Print a message to each of the three people still on your list, letting them know they’re still invited.
print(f"hey {members[0]}, You still invited for pool party💃💃🎉.")
print(f"hey {members[1]}, You still invited for pool party💃💃🎉.")
print(f"hey {members[2]}, You still invited for pool party💃💃🎉.")

#Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
print("Party Ended ❌❌❌❌")
print(f"Im iviting {len(members)} members")
del members[0]
del members[0]
del members[0]
print(f"at the end we have {members} left")
