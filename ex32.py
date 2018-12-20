the_count = [1,2,3,4,5]
fruits = ['Apples','Oranges','Pears','Apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#First kind of for loop
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for i in change: #For mixing types of list
    print(f"I got {i}")

elements = []
#Range function count from 0 to 5
for i in range(0,6):
    print(f"Adding {i} to list")
    elements.append(i)
for i in elements:
    print(f"Element was: {i}")