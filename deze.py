from colorama import *
uu = 0

print("* - множити")
print("** - піднести до степеню")
print("/ - поділити")
a = int(input(" first number"))
c = input("  дія : ")
b = int(input(" second number"))
def assd():
    global uu
    global a
    global b
    global c
    try:
        try:
            if c == "*":
                uu = a*b
                print(uu)
            elif c =="**":
                uu = a**b
                print(uu)
            elif c =="/":
                uu = a/b
                print(uu)
            elif c =="+":
                uu = a+b
                print(uu)
            elif c =="-":
                uu = a-b
                print(uu)
            else:
                print("дія не правильна")
        except ZeroDivisionError:
            print(Fore.RED + " cant divide by 0")
    except ValueError:
        print(Fore.RED + "this version can only run with whole numbers sorry.")



assd()