from sys import argv
from os.path import exists

script, file_from, file_to = argv

#input_file = open(file_from)

#if we use this line. we don't need to close the file
indata = open(file_from).read()
#file closed here by python

if(exists(file_from)):
    print(f"Input file is {len(indata)} bytes long.")
if (exists(file_to)):
    print("Output file exist")


output_file = open(file_to,'w')
output_file.write(indata)
print("Writed to output file")

#input_file.close()
output_file.close()