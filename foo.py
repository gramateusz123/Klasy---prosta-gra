import random

class Character:
    def __init__(self, typ, int, str, hp):
        self.typ = typ
        self.int = int
        self.str = str
        self.hp = hp
class Mage(Character):
    def __init__(self):
        super().__init__(typ="magic", int=15, str=3, hp=52)

class Cleric(Character):
    def __init__(self):
        super().__init__(typ="magic", int=10, str=5, hp=67)

class Warr(Character):
    def __init__(self):
        super().__init__(typ="mele", int=3, str=8, hp=105)

class Barb(Character):
    def __init__(self):
        super().__init__(typ="mele", int=1, str=12, hp=78)

class Mob:
    def __init__(self, typ, int, str, hp):
        self.typ = typ
        self.int = int
        self.str = str
        self.hp = hp

class Wizz(Character):
    def __init__(self):
        super().__init__(typ="magic", int=11, str=4, hp=60)

class Sham(Character):
    def __init__(self):
        super().__init__(typ="magic", int=9, str=8, hp=75)

class Demon(Character):
    def __init__(self):
        super().__init__(typ="mele", int=5, str=9, hp=90)

class Berserk(Character):
    def __init__(self):
        super().__init__(typ="mele", int=1, str=18, hp=70)


mag = Mage()
cler = Cleric()
war = Warr()
barb = Barb()

wizz = Wizz()
shaman = Sham()
demon = Demon()
bers = Berserk()

def profession():
    print("What is your class ?: ")
    print("1. Mage   type:",mag.typ,"  Intelligence:",mag.int,"  Strenght: ",mag.str,"  Health Points: ",mag.hp)
    print("2. Cleric   type:",cler.typ,"  Intelligence:",cler.int,"  Strenght: ",cler.str,"  Health Points: ",cler.hp)
    print("3. Warrior   type:",war.typ,"  Intelligence:",war.int,"  Strenght: ",war.str,"  Health Points: ",war.hp)
    print("4. Barbarian   type:",barb.typ,"  Intelligence:",barb.int,"  Strenght: ",barb.str,"  Health Points: ",barb.hp)
    p_class = input()
    p_class = int(p_class)
    if p_class == 1:
        p_class = mag
    elif p_class == 2:
        p_class = cler
    elif p_class == 3:
        p_class = war
    elif p_class == 4:
        p_class = barb

    return p_class

player_class = profession()

def enemy():
    for x in range(1):
        opp = random.randint(1,4)
        if opp == 1:
            opp = 'Wizzard'
            enemy = wizz
        elif opp == 2:
            opp = "Shaman"
            enemy = shaman
        elif opp == 3:
            opp = "Demon"
            enemy = demon
        elif opp == 4:
            opp = 'Berserk'
            enemy = bers
        print("Your enemy is",opp,"!")
        return enemy


enemy = enemy()

def fight(player_class,enemy):
    if enemy.typ =="mele" and player_class.typ =='mele':
        while(player_class.hp > 0 and enemy.hp > 0):
            player_class.hp -= enemy.str
            print("Enemy hits you for",enemy.str,"!")
            print("You have ",player_class.hp,"HP!")
            if player_class.hp > 0:
                enemy.hp -= player_class.str
                print("You hit an enemy for",player_class.str,"!")
                print("Enemy have ", enemy.hp, "HP!")
        if player_class.hp <= 0:
            print("You have been defeated!")
        elif enemy.hp <= 0:
            print("You win! You have still",player_class.hp,"HP!")
        return(player_class.hp)

    elif enemy.typ =="magic" and player_class.typ =='mele':
        while (player_class.hp > 0 and enemy.hp > 0):
            player_class.hp -= enemy.int
            print("Enemy hits you for", enemy.int, "!")
            print("You have ", player_class.hp, "HP!")
            if player_class.hp > 0:
                enemy.hp -= player_class.str
                print("You hit an enemy for", player_class.str, "!")
                print("Enemy have ", enemy.hp, "HP!")
        if player_class.hp <= 0:
            print("You have been defeated!")
        elif enemy.hp <= 0:
            print("You win! You have still",player_class.hp,"HP!")
        return(player_class.hp)

    elif enemy.typ =="mele" and player_class.typ =='magic':
        while (player_class.hp > 0 and enemy.hp > 0):
            player_class.hp -= enemy.str
            print("Enemy hits you for", enemy.int, "!")
            print("You have ", player_class.hp, "HP!")
            if player_class.hp > 0:
                enemy.hp -= player_class.int
                print("You hit an enemy for", player_class.int, "!")
                print("Enemy have ", enemy.hp, "HP!")
        if player_class.hp <= 0:
            print("You have been defeated!")
        elif enemy.hp <= 0:
            print("You win! You have still", player_class.hp,"HP!")
        return(player_class.hp)

    elif enemy.typ =="magic" and player_class.typ =='magic':
        while (player_class.hp > 0 and enemy.hp > 0):
            player_class.hp -= enemy.int
            print("Enemy hits you for", enemy.int, "!")
            print("You have ", player_class.hp, "HP!")
            if player_class.hp > 0:
                enemy.hp -= player_class.int
                print("You hit an enemy for", player_class.int, "!")
                print("Enemy have ",enemy.hp,"HP!")
        if player_class.hp <= 0:
            print("You have been defeated!")
        elif enemy.hp <= 0:
            print("You win! You have still",player_class.hp,"HP!")
        return(player_class.hp)

walka = fight(player_class,enemy)

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


