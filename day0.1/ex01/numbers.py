def display_numbers():
    """Read a file and display each numbers"""

    file = open("numbers.txt", "r")
    content = file.read()
    file.close()

    numbers = content.split(",")

    for number in numbers:
        print(number)


if __name__ == '__main__':
    display_numbers()