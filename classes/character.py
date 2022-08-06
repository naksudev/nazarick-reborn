class Character:
    def __init__(self, name, health, attack, defense, speed, inv):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.inv = inv

    def dealDamage(self, target):
        damage = self.attack * (10 / (10 + target.defense))
        target.health = target.health - damage
        print("==============================")
        print("⚔ {:} attacked {:}".format(self.name, target.name))

    def defend(self):
        print("==============================")
        print("🛡 {:} defended !".format(self.name))

    # def addItem(self, item):
    #     self.inv.append(item)
