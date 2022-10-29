import inspect
import requests
import sys
data = "string"

print(hasattr(data, "reverse"))
print(hasattr(data, "index"))

def data2():
    pass
print(callable(data))
print(callable(data2))
print(inspect.ismodule(data2))
print(inspect.isclass(data2))
print(inspect.isfunction(data2))

print(sys.platform)