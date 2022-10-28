import random
class solider1:
    def __init__(self):
        self.name = solider1
        self.health = 100
        self.strength = random.randint(1,6)
        self.stamina =random.randint(1,6)
        self.speed = random.randint(1,4)
class solider2:
    def __init__(self):
        self.name = solider2
        self.health = 100
        self.strength = random.randint(1,6)
        self.stamina =random.randint(1,6)
        self.speed = random.randint(1,4)
class solider3:
    def __init__(self):
        self.name = solider3
        self.health = 100
        self.strength = random.randint(1,6)
        self.stamina =random.randint(1,6)
        self.speed = random.randint(1,4)
class solider4:
    def __init__(self):
        self.name = solider4
        self.health = 100
        self.strength = random.randint(1,6)
        self.stamina =random.randint(1,6)
        self.speed = random.randint(1,4)

sol1 = solider1()
sol2 = solider2()
sol3 = solider3()
sol4 = solider4()

goodsol1 =[]
goodsol2 =[]
class pvp:
    def firstpart(self):

        global goodsol1
        global goodsol2
        sol1.health -= sol2.strength*sol2.stamina
        sol2.health -= sol1.strength*sol1.stamina
        if sol1.health > sol2.health:
            goodsol1 = 1
        elif sol1.health == sol2.health:
            if random.randint(1, 2) == 1:
                goodsol1 = 1
            else:
                goodsol1 = 2
        else:
            goodsol1 = 2


        sol3.health -= sol4.strength * sol4.stamina
        sol4.health -= sol3.strength * sol3.stamina
        if sol3.health > sol4.health:
            goodsol2 = 3
        elif sol3.health == sol4.health:
            if random.randint(1, 2) == 1:
                goodsol2 = 3
            else:
                goodsol2 = 4

        else:
            goodsol2 = 4
        print(sol1.health)
        print(sol2.health)
        print(sol3.health)
        print(sol4.health)
        if goodsol1 == 1 :
            if goodsol2 == 3:
                sol1.health -= sol3.strength * sol3.stamina
                sol3.health -= sol1.strength * sol1.stamina
                if sol1.health > sol3.health:
                    print("SOLIDER 1 WON!!!!!")
                elif sol1.health == sol3.health:
                    if random.randint(1, 2) == 1:
                        print("SOLIDER 1 WON!!!!!")
                    else:
                        print("SOLIDER 3 WON!!!!!")
                elif sol1.health < sol3.health:
                    print("SOLIDER 3 WON!!!!!")
            elif goodsol2 == 4:
                sol1.health -= sol4.strength * sol4.stamina
                sol4.health -= sol1.strength * sol1.stamina
                if sol1.health > sol4.health:
                    print("SOLIDER 1 WON!!!!!")
                elif sol1.health == sol4.health:
                    if random.randint(1, 2) == 1:
                        print("SOLIDER 1 WON!!!!!")
                    else:
                        print("SOLIDER 4 WON!!!!!")
                elif sol1.health < sol4.health:
                    print("SOLIDER 4 WON!!!!!")
        elif goodsol1 == 2:

            if goodsol2 == 3:
                sol2.health -= sol3.strength * sol3.stamina
                sol3.health -= sol2.strength * sol2.stamina
                if sol2.health > sol3.health:
                    print("SOLIDER 2 WON!!!!!")
                elif sol1.health == sol3.health:
                    if random.randint(1, 2) == 1:
                        print("SOLIDER 2 WON!!!!!")
                    else:
                        print("SOLIDER 3 WON!!!!!")
                elif sol2.health < sol3.health:
                    print("SOLIDER 3 WON!!!!!")
            elif goodsol2 == 4:
                sol2.health -= sol4.strength * sol4.stamina
                sol4.health -= sol2.strength * sol2.stamina
                if sol2.health > sol4.health:
                    print("SOLIDER 2 WON!!!!!")
                elif sol2.health == sol4.health:
                    if random.randint(1, 2) == 1:
                        print("SOLIDER 2 WON!!!!!")
                    else:
                        print("SOLIDER 4 WON!!!!!")
                elif sol2.health < sol4.health:
                    print("SOLIDER 4WON!!!!!")
        print(sol1.health)
        print(sol2.health)
        print(sol3.health)
        print(sol4.health)
PPP = pvp()
PPP.firstpart()
