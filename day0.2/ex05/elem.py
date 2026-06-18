#!/usr/bin/python3


class Text(str):
    # Text inherits from Python str class

    def __str__(self):
        # super().__str__() get normal string then 
        # replace special HTML char to display as text instead of being interpreted as HTML
        # Then we replace special HTML characters so they are displayed
        # as text instead of being interpreted as HTML.
        # Ex: Text("<h1>") becomes "&lt;h1&gt;"

        return (super().__str__()
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace('\n', '\n<br />\n'))


class Elem:
    #One HTML element.
    #Ex:
    #Elem("h1", content=Text("Hello")) render as:
    # <h1>
    #   Hello
    # </h1>

    class ValidationError(Exception):
        #exception for invalid content passed to Elem.
        pass

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        """init object with tag, attribute, content and tag_type (simple or double)"""

        self.tag = tag
        self.attr = attr
        self.tag_type = tag_type

        self.content = [] # Content stored internally as list.

        if content is not None:

            if not Elem.check_type(content): #Check if content is HTML compatible
                raise Elem.ValidationError

            self.add_content(content)

    def __str__(self):
        # Converts Elem object into HTML string

        if self.tag_type == 'double': #tag goes before and after
            result = "<" + self.tag + self.__make_attr() + ">"
            result += self.__make_content()
            result += "</" + self.tag + ">"

        elif self.tag_type == 'simple': #tag only goes before
            result = "<" + self.tag + self.__make_attr() + " />"

        return result

    def __make_attr(self):
        # Builds HTML attributes string
        # Ex: {"src": "image.jpg", "alt": "photo"} -> alt="photo" src="image.jpg"
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        # converts all child content into HTML and add indentation

        if len(self.content) == 0:
            # Empty double tag: <div></div>
            return ''

        # new line after content
        result = '\n'

        for elem in self.content:
            lines = str(elem).split('\n')

            for line in lines:
                result += '  ' + line + '\n'

        return result

    def add_content(self, content):
        # Adds content after the Elem has been created

        if not Elem.check_type(content):# Reject invalid content
            raise Elem.ValidationError

        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')] #skip empty elements

        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        # Check if content is valid

        return (
            isinstance(content, Elem)
            or type(content) == Text
            or (
                type(content) == list
                and all(
                    [
                        type(elem) == Text or isinstance(elem, Elem)
                        for elem in content
                    ]
                )
            )
        )


if __name__ == '__main__':
    pass