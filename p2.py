class Student:
    print("hi")
    def __init__(self, height=160):
        self.height = height



vasa = Student()
print(vasa.height)
dima = Student(height=188)
print(dima.height)
print(vasa.height)