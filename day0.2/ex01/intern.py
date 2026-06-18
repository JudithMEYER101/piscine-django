class Intern:

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    #Init with default name (replace if given a name)
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    #Define what print(object) shows
    def __str__(self):
        return self.Name #Store name inside object

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    #Create the coffe object inside Intern
    def make_coffee(self):
        return Intern.Coffee()


def test():
    """Creates to object Intern one with default name (intern) 
       and one named Mark. Ask Mark to make coffee and intern to work"""

    intern = Intern()
    mark = Intern("Mark")

    print(intern)
    print(mark)

    coffee = mark.make_coffee()
    print(coffee)

    try:
        intern.work()
    except Exception as error:
        print(error)


if __name__ == '__main__':
    test()