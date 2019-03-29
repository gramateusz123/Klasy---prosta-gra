import random
from statystyki import stats
class Character:
    def __init__(self, typ, hp):
        self.typ = typ          #usunięty int i strg, kod do poprawy
        self.hp = hp
class Mage(Character):
    def __init__(self, mana, typ, hp):
        super().__init__(typ, hp)
        self.mana = mana
    def frostBolt(self,damage):
        print("Casting Frost Bolt !")
        self.mana -= 15
        return damage

class Cleric(Mage):
    def __init__(self, typ, hp, mana):
        super().__init__(typ, hp, mana)
    def healingTouch(self):
        print("Healing yourself! ")
        self.hp += random.randint(15,40)

class Warrior(Character):
    def __init__(self,typ,hp,stamina,strg):
        super().__init__(typ,hp)
        self.stamina = stamina
    def critStrike(self,strg):
        print("Critical strike ! ")
        self.stamina -= 10
        strg += 20
        return strg

class Barbarian(Character):
    def __init__(self,typ,hp,stamina,strg):
        super().__init__(typ,hp,stamina,strg)
    def berserkStance(self,strg,hp):
        print("Entering Berserker Stance!")
        self.stamina += 30
        self.strg += 10


class Mob:
    def __init__(self, typ, int, strg, hp):
        self.typ = typ
        self.hp = hp

class Wizzard(Mage):
    def __init__(self,typ,hp,mana):
        super().__init__(typ,hp,mana)

class Shaman(Mage):
    def __init__(self,typ,hp,mana):
        super().__init__(typ,hp,mana)

class Demon(Warrior):
    def __init__(self,typ,hp,stamina,strg):
        super().__init__(typ,hp,stamina,strg)
        strg += 5

class Berserk(Warrior):
    def __init__(self,typ,hp,stamina,strg):
        super().__init__(typ,hp,stamina,strg)
        stamina += 5
        strg += 3


def profession():
    loop = 1
    while loop == 1:
        print("What is your class ?: ")
        print("1. Mage")
        print("2. Cleric")
        print("3. Warrior")
        print("4. Barbarian")
        print("To see statictics, type STATS")
        p_class = input()

        #if p_class == "stats" or "STATS" or "Stats":
        #    stats()
        #   p_class = input()
        if p_class == 1:
            mage = Mage(random.randint(70,95), random.randint(90,120), "magic")
            p_class = mage
            loop = 0
            return p_class
        elif p_class == 2:
            cleric = Cleric(random.randint(90,130), random.randint(60,90), "magic/healing")
            p_class = cleric
            return p_class
            loop = 0
        elif p_class == 3:
            warrior = Warrior(random.randint(150,200), random.randint(10,18),40, "tank")
            p_class = warrior
            return p_class
            loop = 0
        elif p_class == 4:
            barbarian = Barbarian("mele",random.randint(130,160),30,random.randint(22-30))
            p_class = barbarian
            return p_class
            loop = 0


player_class = profession()
print(player_class)

def enemy():
    for x in range(1):
        opp = random.randint(1,4)
        if opp == 1:
            opp = 'Wizzard'
            wizzard = Wizzard()
            enemy = wizzard
        elif opp == 2:
            opp = "Shaman"
            shaman = Shaman()
            enemy = shaman
        elif opp == 3:
            opp = "Demon"
            demon = Demon()
            enemy = demon
        elif opp == 4:
            opp = 'Berserk'
            berserk = Berserk()
            enemy = berserk
        print("Your enemy is",opp,"!")
        return enemy


enemy = enemy()



def elixir(hp_healed):
    player_class.hp += hp_healed
    return player_class.hp

print("What do you want do to?")
print("1. Use health elixir")
decision1 = input()
if decision1 == "1":
    hp_healed = random.randint(1,25)
    elixir(hp_healed)
    print("You healed",hp_healed,"HP!")
    print("You have",player_class.hp,"HP!")


