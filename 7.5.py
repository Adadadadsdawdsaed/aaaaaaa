def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We hav prablim {exc}")
        else:
            print(f"no error, result is {result}")
    return checker
def calc(expression):
    return eval(expression)
calc = checker(calc)
calc("23+4")
