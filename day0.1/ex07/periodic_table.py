def parse_element(line):
    """creat a dict for a line ex:
       Hydrogen = position:0, number:1, small: H, molar:1.00794, electron1"""

    name, data = line.split(" = ") #separate name and data
    fields = data.split(", ") #separates datas from each other (pos, num, etc..)

    element = {"name": name}

    #Build dict (key = name, value = hydorgen, etc...)
    for field in fields:
        key, value = field.split(":")
        element[key] = value.strip()

    return element


def read_elements():
    """ Read the whole file and return a list of dict with parse element"""

    try:
        file = open("periodic_table.txt", "r")
    except FileNotFoundError:
        print("Error: periodic_table.txt not found.")
        return []

    lines = file.readlines()
    file.close()

    elements = []

    #for each line append to the list the new element dict
    for line in lines:
        line = line.strip()
        if line:
            elements.append(parse_element(line))

    return elements


def write_empty_cell(file):
    """ Write an empty table cell """

    file.write('<td style="border: 1px solid black; padding:10px"></td>\n')


def write_element_cell(file, element):
    """Generate a table cell from the data in element"""

    file.write('<td style="border: 1px solid black; padding:10px">\n')
    file.write('<h4>' + element["name"] + '</h4>\n')
    file.write('<ul>\n')
    file.write('<li>No ' + element["number"] + '</li>\n')
    file.write('<li>' + element["small"] + '</li>\n')
    file.write('<li>' + element["molar"] + '</li>\n')
    file.write('<li>' + element["electron"] + ' electron</li>\n')
    file.write('</ul>\n')
    file.write('</td>\n')


def create_html(elements):
    """Create an HTML file of the periodic element table from list of dict element"""

    file = open("periodic_table.html", "w")

    #Write HTML skeletton
    file.write('<!DOCTYPE html>\n')
    file.write('<html lang="en">\n')
    file.write('<head>\n')
    file.write('<meta charset="utf-8">\n')
    file.write('<title>Periodic Table</title>\n')
    file.write('</head>\n')
    file.write('<body>\n')
    file.write('<h1>Periodic Table of Elements</h1>\n')
    file.write('<h2>Elements</h2>\n')
    file.write('<h3>List</h3>\n')

    file.write('<table style="border-collapse: collapse;">\n')

    current_position = 0 #tracks index in current row
    file.write('<tr>\n')

    for element in elements:
        element_position = int(element["position"])

        # New row starts when position resets to 0
        if element_position == 0 and current_position != 0:
            while current_position < 18:
                write_empty_cell(file)
                current_position += 1

            file.write('</tr>\n')
            file.write('<tr>\n')
            current_position = 0

        # Fill empty spaces before element
        while current_position < element_position:
            write_empty_cell(file)
            current_position += 1

        # Write the actual element
        write_element_cell(file, element)
        current_position += 1

    # Fill remaining cells in last row
    while current_position < 18:
        write_empty_cell(file)
        current_position += 1

    file.write('</tr>\n')
    file.write('</table>\n')
    file.write('</body>\n')
    file.write('</html>\n')

    file.close()


def periodic_table():
    """ Create a list of dict element from a .txt then create an HTML
        Periodic table from that dict"""

    elements = read_elements()
    create_html(elements)


if __name__ == '__main__':
    periodic_table()