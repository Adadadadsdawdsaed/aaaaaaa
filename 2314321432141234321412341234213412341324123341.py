import time

def printer():

    for i in range(100000):
        print("hi")
start_time = time.time()
printer()
print(" %s seconds" % (time.time() - start_time))


