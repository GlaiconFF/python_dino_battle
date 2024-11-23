
class Dinosaur: 
    def __init__(self, name, attack, hp, speed) -> None:
        self.name = name
        self.attack = attack
        self.hp = hp
        self.speed = speed

    def __str__(self) -> str:
        return f"Name: {self.name} | Attack: {self.attack} | HP: {self.hp}"
    
    def basic_attack(self, enemy):
        damage_dealt = self.attack
        enemy.hp -= damage_dealt
        return damage_dealt 

class Teeths(Dinosaur):
    def __init__(self, name, attack, hp, speed) -> None:
        super().__init__(name, attack, hp, speed)
    def special_attack(self, enemy):
        damage_dealt = self.attack
        enemy.hp -= damage_dealt*2
        return damage_dealt 

class Claws(Dinosaur):
    def __init__(self, name, attack, hp, speed) -> None:
        super().__init__(name, attack, hp, speed)

class Armor(Dinosaur):
    def __init__(self, name, attack, hp, speed) -> None:
        super().__init__(name, attack, hp, speed)

def combat(enemy, ataque_escolhido):
    ataque_escolhido(enemy)

def create():
    dino1 = Teeths("Tyrannosaur Rex", 60, 100, 110)
    dino2 = Claws("Velociraptor", 40, 70, 120)
    dino3 = Armor("Triceratops", 20, 130, 100)
    #print(dino1, dino2, dino3, sep="\n")
    return dino1, dino2, dino3

if __name__ == "__main__":
    dinos = create()
    for dino in dinos:
        print(dino)
    ataque_escolhido = int(input("Escolha um ataque:\nAtaque básico - 1\nAtaque especial - 2\n"))
    if ataque_escolhido == 1:
        ataque_escolhido = dinos[0].basic_attack
    elif ataque_escolhido == 2:
        ataque_escolhido = dinos[0].special_attack
    else:
        ataque_escolhido = dinos[0].basic_attack
    combat(dinos[1], ataque_escolhido)
    for dino in dinos:
        print(dino)
    



