class character:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed

    def attack(self, other_character):
        damage = self.attack_power - other_character.defense
        if damage < 0:
            damage = 0
        other_character.health -= damage
        print(f"{self.name} attacks {other_character.name} for {damage} damage!")
        if other_character.health <= 0:
            print(f"{other_character.name} has been defeated!")
            return True
        return False

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} is defeated!")
            return True
        return False

    def is_alive(self):
        if self.health <= 0:
            return False
        return True

class warrior(character):
    def __init__(self, name, health, attack_power, defense, speed,rage):
        super().__init__(name, health, attack_power, defense, speed)
        self.rage=rage
    def boost_attack(self):
        if self.rage==100 or self.health<=30:
            damage=self.attack_power*2-self.defense
            if damage<0:
                damage=0
            self.rage-=10
            print(f"{self.name} boosts attack for 10 rage!")
            return damage
        else:
            print(f"{self.name} does not have enough rage to boost attack.")
        
class mage(character):
    def __init__(self, name, health, attack_power, defense, speed,mana):
        super().__init__(name, health, attack_power, defense, speed,)
        self.mana=mana
    def cast_spell(self,other_character):
        if self.mana>=10:
            damage=self.attack_power*2-other_character.defense
            if damage<0:
                damage=0
            other_character.health-=damage
            self.mana-=10
            print(f"{self.name} casts a spell on {other_character.name} for {damage} damage!")
            if other_character.health<=0:
                print(f"{other_character.name} has been defeated!")
                return True
        else:
            print(f"{self.name} does not have enough mana to cast a spell.")
        return False

class archer(character):
    def __init__(self, name, health, attack_power, defense, speed):
        super().__init__(name, health, attack_power, defense, speed)
    def shoot_arrow(self,other_character):
        damage=self.attack_power*2-other_character.defense
        if damage<0:
            damage=0
        other_character.health-=damage
        print(f"{self.name} shoots an arrow at {other_character.name} for {damage} damage!")
        if other_character.health<=0:
            print(f"{other_character.name} has been defeated!")
            return True
        return False
    
class battle:
    def __init__(self,character1,character2,character3):
        self.character1=character1
        self.character2=character2
        self.character3=character3
       
    def start(self):
        while self.character1.is_alive() and self.character2.is_alive() and self.character3.is_alive():
            if self.character1.speed>self.character2.speed and self.character1.speed>self.character3.speed:
                if self.character1.attack(self.character2):
                    break
                if self.character2.attack(self.character1):
                    break
                if self.character3.attack(self.character1):
                    break
            elif self.character2.speed>self.character1.speed and self.character2.speed>self.character3.speed:
                if self.character2.attack(self.character2):
                    break
                if self.character1.attack(self.character1):
                    break
                if self.character3.attack(self.character1):
                    break
            else:
                if self.character2.attack(self.character1):
                    break
                if self.character1.attack(self.character2):
                    break
                if self.character3.attack(self.character1):
                    break
        if self.character1.is_alive() and self.character2.is_alive() and self.character3.is_alive():
            print("All characters are alive!")
        elif self.character1.is_alive() and self.character2.is_alive():
            print(f"{self.character1.name} and {self.character2.name} are alive!")
        elif self.character1.is_alive() and self.character3.is_alive():
            print(f"{self.character1.name} and {self.character3.name} are alive!")
        elif self.character2.is_alive() and self.character3.is_alive():
            print(f"{self.character2.name} and {self.character3.name} are alive!")
        print("Battle is over!")
        if self.character1.is_alive():
            print(f"{self.character1.name} wins!")
        else:
            print(f"{self.character2.name} wins!")

if __name__=="__main__":
    character1=warrior("Warrior",100,20,10,5,0)
    character2=mage("Mage",80,15,5,10,0)
    character3=archer("Archer",70,10,5,15)
    battle1=battle(character1,character2,character3)
    battle1.start()