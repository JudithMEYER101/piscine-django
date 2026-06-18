class HotBeverage:

    price = 0.30
    name = "hot beverage"

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return (
            "name : " + self.name + "\n"
            + "price : " + format(self.price, ".2f") + "\n"
            + "description : " + self.description()
        )


#Need to change every value
class Coffee(HotBeverage):
    price = 0.40
    name = "coffee"

    def description(self):
        return "A coffee, to stay awake."


#Don't need any change apart from the name
class Tea(HotBeverage):
    name = "tea"

#Need to change every value
class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"

    def description(self):
        return "Chocolate, sweet chocolate..."

#Need to change every value
class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"

    def description(self):
        return "Un po' di Italia nella sua tazza!"


def test():
    """ Creates all beverages and print their str"""

    beverages = [
        HotBeverage(),
        Coffee(),
        Tea(),
        Chocolate(),
        Cappuccino()
    ]

    for beverage in beverages:
        print(beverage)
        print()


if __name__ == '__main__':
    test()