import random
class Rifle:
    def __init__(self):
        self.mass = 0
        self.accuracy = 0
        self.rif = random.randint(1,4)
    def chosing(self):
        if self.rif == 1:
            self.mass +=0
            self.accuracy +=1
        elif self.rif == 2:
            self.mass += 1
            self.accuracy += 1
        elif self.rif == 3:
            self.mass += 3
            self.accuracy += 1
        elif self.rif == 4:
            self.mass += 2
            self.accuracy += 3
RIFEL = Rifle()
RIFEL.chosing()
a = RIFEL.mass
b = RIFEL.accuracy
print(a)
print(b)
class sniper:


    def __init__(self):
        self.accuracy = random.randint(1,4) - b
        self.strength = random.randint(1,4) - a
        self.concentration = random.randint(1, 4)
        self.shoot = 0
        self.fire = 0
        self.alive = True
    def mission(self):

        self.fire = self.accuracy + self.strength + self.concentration

        if self.fire <= 3:
            self.shoot = 1
        elif self.fire >= 4 and self.fire <= 6:
            self.shoot = 2

        elif self.fire >= 7 and self.fire <= 11:
           self.shoot = 4
        else:
            self.shoot = 6

        if self.shoot == 1:
            print("mission succeed!!")
        elif self.shoot == 2:
            if random.randint(1, 2) == 1:
                print("mission succeed!!")
            else:
                print("you were killed by soneone during reloading")
                self.alive = False
        elif self.shoot == 4:
            if random.randint(1, 4) == 1:
                print("mission succeed!!")
            else:
                print("you were killed by soneone during reloading")
                self.alive = False
        elif self.shoot == 6:
            if random.randint(1, 6) == 1:
                print("mission succeed!!")
            else:
                print("you were killed by soneone during reloading")
                self.alive = False

Sinper = sniper()
for day in range(1,8):
    if Sinper.alive == False:
        break
    else:
        day +=1
        print(f"======================day {day - 1}=========================")
        Sinper.mission()
        print(f"{Sinper.strength} strength")
        print(f"{Sinper.accuracy} accuracy")
        print(f"{Sinper.concentration} concentration")
        print(f"{Sinper.fire} fire")
        print(f"{Sinper.shoot} shoot")
if Sinper.alive == True:
    print("you did it!")




