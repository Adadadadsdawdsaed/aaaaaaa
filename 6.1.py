try:
    print("start")
    print(10/0)
    print("end, no error")
except NameError:
    print("error")

except ZeroDivisionError:
    print("skill issue")