import random


class Pokemon:
    def __init__(self, name, hp, element):
        self.name = name
        self.hp = hp
        self.element = element
    
    def doMove(self):
        print("Pokemon moving")

    def doEat(self):
        print("Pokemon eating")

class JigglyPuff(Pokemon):
    def __init__(self, name, hp, element, lungcapacity):
        super().__init__(name, hp, element)
        self.lungcapacity = lungcapacity

    def doMove(self):
        super().doMove()
        print("JigglyPuff can float")

    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.hp}\nElement: {self.element}\nLung Capacity: {self.lungcapacity}"

class Pikachu(Pokemon):
    def __init__(self, name, hp, element, color, electricity):
        super().__init__(name, hp, element)
        self.color = color
        self.electricity = electricity

    def __str__(self):
        return f"Name: {self.name}\nHealth: {self.hp}\nElement: {self.element}\nColor: {self.color}\nElectricity: {self.electricity}"

class Game:
    def __init__(self):
        self.elements = ["thunder", "ice", "fire", "ghost", "water"]

        self.pokemons = {
            "jigglypuff": [JigglyPuff(f"J{i}", random.randint(50, 100), random.choice(self.elements), random.randint(50, 100)) for i in range(random.randint(3, 15))],
            "Pikachu": [Pikachu(f"P{i}", random.randint(50, 100), random.choice(self.elements), "Yellow", random.randint(50, 100)) for i in range(random.randint(5, 20))]
        }

    def __str__(self):
        message = ""
        for pokemonname, pokemonlist in self.pokemons.items():
            for pokemon in pokemonlist:
                message += str(pokemon) + "\n" + "-" * 20 + "\n"
        return message

game = Game()
print(game)

# class Weapon():
#     def __init__(self):
#         pass

# class Thunderbolt(Weapon):
#     def __init__(self):
#         super().__init__()
#         pass

# class Fireball (Weapon):
#     def __init__(self):
#         super().__init__()
#         pass

# pokemon = JigglyPuff("J1", 75, "fairy", 92)
# pokemon.doMove()