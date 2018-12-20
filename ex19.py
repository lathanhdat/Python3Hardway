def check_function(arg1,arg2):
    print(f"arg1 = {arg1}, arg2 = {arg2}.")

a = 100
b = 200
check_function(100,200)
check_function(a,b)
check_function(100+5,200/2)
check_function(a+5,b/2)

c = int(input("Input first number: "))
d = int(input("Input second number: "))
check_function(c,d)