#asterisk args which a lot like your argv but for function.
#this is not a normal way to do
def print_two(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


#We'll use this way
def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

print_two("Hello","World!")
print_two_again("Hello","World!")