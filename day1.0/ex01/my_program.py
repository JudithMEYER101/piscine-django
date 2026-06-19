from path import Path


def my_program():
    """ Using the Path library to create a file and a folder
        Write in the folder and print it's content"""

    folder = Path("my_folder")
    file = folder / "my_file.txt"

    folder.makedirs_p()

    file.write_text("This is a Text from path.py/my_file.txt\n")

    print(file.read_text())


if __name__ == '__main__':
    try:
        my_program()
    except Exception as error:
        print("Error:", error)