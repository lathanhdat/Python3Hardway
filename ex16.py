from sys import argv
script, filename = argv

print("Opening the file:")
fd = open(filename,'w')
print("Truncating the file:")
fd.truncate()
print("Input three line:")
line1 = input("Input line 1: ")
line2 = input("Input line 2: ")
line3 = input("Input line 3: ")

data_print = "{}\n{}\n{}\n"

fd.write(data_print.format(line1,line2,line3))


#Close and save file
fd.close()