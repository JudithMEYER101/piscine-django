import sys
import os
import re
import settings


def check_arguments():
    """Verify user input"""

    if len(sys.argv) != 2:
        raise Exception("Error: wrong number of arguments")

    filename = sys.argv[1]

    if not filename.endswith(".template"): #Check extension
        raise Exception("Error: file must have .template extension")

    if not os.path.isfile(filename): #Check file exist
        raise Exception("Error: file does not exist")

    return filename


def read_template(filename):
    """Open file, reads it and returns content as a string"""

    file = open(filename, "r") #Open in read mod
    content = file.read()
    file.close()
    return content


def replace_variables(content):
    """Replace placeholder with real values"""

    variables = settings.__dict__ #get variable in settings as a dict

    for key in variables:
        if not key.startswith("__"):  #ignore python internal variable (ex: __name__)
            pattern = "{" + key + "}" #ex : pattern = {name}
            content = re.sub(pattern, str(variables[key]), content) #ex: <h1>{name}</h1> becomes <h1>Judith</h1>

    return content


def write_html(filename, content):
    """Write HTML file with variable replaced through replace_variable()"""

    output_filename = filename.replace(".template", ".html")

    file = open(output_filename, "w") #open in write mod
    file.write(content)
    file.close()


def render():
    """ Use value from settings.py to replace placeholder in .template
        then write new HTML file"""

    filename = check_arguments()
    content = read_template(filename)
    content = replace_variables(content)
    write_html(filename, content)


if __name__ == '__main__':
    try:
        render()
    except Exception as error:
        print(error)