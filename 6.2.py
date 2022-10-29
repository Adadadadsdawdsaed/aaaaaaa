try:
    try:
        print("start")
        print(hello)
        print("end no error")
    except SyntaxError:
        print("Wrong syntax")

except NameError as error:
    print(error)
