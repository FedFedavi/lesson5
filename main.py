class Warrior():

    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел поесть")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет когото")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"имя воина {self.name}")
        print(f"сила воина {self.power}")
        print(f"выносливость воина {self.endurance}")
        print(f"цвет волос воина {self.hair_color}")

war1 = Warrior("Степа", 76, 54, "коричневый")
war2 = Warrior("Егор", 45, 23, "блонд")

war1.info()
war1.sleep()
war1.eat()
war1.hit()
war1.walk()
war1.info()

war2.info()
war2.sleep()
war2.eat()
war2.hit()
war2.walk()
war2.info()

sleep()