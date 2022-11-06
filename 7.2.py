def raide_to_degree(number, degree):
    i = 0

    while True:
        result = number**i
        yield result
        if result > 1000**20:
            break
        i +=1

res = raide_to_degree(1234, 500)
print(res)
for _ in res:
    print(_)
    print("----")