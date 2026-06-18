import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:

    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            Exception.__init__(self, "This coffee machine has to be repaired.")

    def __init__(self):
        self.served = 0
        self.broken = False

    def repair(self):
        self.served = 0
        self.broken = False

    #serve function increase served by 1 at every service then breack at 10
    #From 10 raise broken exception until repair() is called 
    def serve(self, beverage):
        if self.broken:
            raise CoffeeMachine.BrokenMachineException()

        if self.served >= 10:
            self.broken = True
            raise CoffeeMachine.BrokenMachineException()

        self.served += 1

        if random.randint(0, 1) == 0:
            return beverage()
        return CoffeeMachine.EmptyCup()


def test_machine():
    """ Do a cycle of servings until the machine breack then repair and
        do an other cycle"""

    machine = CoffeeMachine()
    drinks = [HotBeverage, Coffee, Tea, Chocolate, Cappuccino]

    print("First cycle:")
    try:
        while True:
            drink = random.choice(drinks)
            print(machine.serve(drink))
            print()
    except CoffeeMachine.BrokenMachineException as error:
        print(error)

    print("\nRepairing machine...\n")
    machine.repair()

    print("Second cycle:")
    try:
        while True:
            drink = random.choice(drinks)
            print(machine.serve(drink))
            print()
    except CoffeeMachine.BrokenMachineException as error:
        print(error)


if __name__ == '__main__':
    test_machine()