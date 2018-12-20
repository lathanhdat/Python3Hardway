i = 0
numbers = []

while i < 6:
    print(f"Top i = {i}")
    numbers.append(i)
    i += 1
    print(f"Bottom i = {i}")

for num in numbers:
    print(num)