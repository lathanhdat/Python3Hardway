ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Not enough 10 things")
stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items.")

print("We have: ",stuff)
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))

#Slice form 3 to 4 and join
print('#'.join(stuff[3:5]))