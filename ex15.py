from sys import argv
script, filename = argv

fd = open(filename)
prompt = '>'

print(f"Here is your {filename}:")
print(fd.read())


print("Chose another file")
filename = input(prompt)
fd = open(filename)
print(f"Here is your {filename}:")
print(fd.read())