#!/usr/bin/python3

from elem import Elem, Text
from elements import *


class Page:
    valid_types = (
        Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td,
        Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text
    )

    def __init__(self, elem):
        self.elem = elem

    def __str__(self):
        if isinstance(self.elem, Html):
            return "<!DOCTYPE html>\n" + str(self.elem)
        return str(self.elem)

    def write_to_file(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def is_valid(self):
        return self.__is_valid_node(self.elem)

    def __is_valid_node(self, node):
        if not isinstance(node, Page.valid_types):
            return False

        if isinstance(node, Text):
            return True

        for child in node.content:
            if not self.__is_valid_node(child):
                return False

        if isinstance(node, Html):
            return self.__valid_html(node)

        if isinstance(node, Head):
            return self.__valid_head(node)

        if isinstance(node, (Body, Div)):
            return self.__valid_body_div(node)

        if isinstance(node, (Title, H1, H2, Li, Th, Td)):
            return self.__valid_single_text(node)

        if isinstance(node, P):
            return self.__valid_p(node)

        if isinstance(node, Span):
            return self.__valid_span(node)

        if isinstance(node, (Ul, Ol)):
            return self.__valid_list(node)

        if isinstance(node, Tr):
            return self.__valid_tr(node)

        if isinstance(node, Table):
            return self.__valid_table(node)

        return isinstance(node, (Meta, Img, Hr, Br))

    def __valid_html(self, node):
        return (
            len(node.content) == 2
            and isinstance(node.content[0], Head)
            and isinstance(node.content[1], Body)
        )

    def __valid_head(self, node):
        return (
            len(node.content) == 1
            and isinstance(node.content[0], Title)
        )

    def __valid_body_div(self, node):
        allowed = (H1, H2, Div, Table, Ul, Ol, Span, Text)

        for child in node.content:
            if not isinstance(child, allowed):
                return False

        return True

    def __valid_single_text(self, node):
        return (
            len(node.content) == 1
            and isinstance(node.content[0], Text)
        )

    def __valid_p(self, node):
        for child in node.content:
            if not isinstance(child, Text):
                return False

        return True

    def __valid_span(self, node):
        for child in node.content:
            if not isinstance(child, (Text, P)):
                return False

        return True

    def __valid_list(self, node):
        if len(node.content) == 0:
            return False

        for child in node.content:
            if not isinstance(child, Li):
                return False

        return True

    def __valid_tr(self, node):
        if len(node.content) == 0:
            return False

        has_th = False
        has_td = False

        for child in node.content:
            if isinstance(child, Th):
                has_th = True
            elif isinstance(child, Td):
                has_td = True
            else:
                return False

        return not (has_th and has_td)

    def __valid_table(self, node):
        for child in node.content:
            if not isinstance(child, Tr):
                return False

        return True


def test():
    valid_page = Page(
        Html([
            Head([
                Title(Text("Hello"))
            ]),
            Body([
                H1(Text("Welcome")),
                Div([
                    H2(Text("Subtitle")),
                    Span([
                        Text("Some text"),
                        P(Text("inside span"))
                    ]),
                    Ul([
                        Li(Text("First")),
                        Li(Text("Second"))
                    ]),
                    Table([
                        Tr([
                            Th(Text("Name")),
                            Th(Text("Age"))
                        ]),
                        Tr([
                            Td(Text("Judith")),
                            Td(Text("25"))
                        ])
                    ])
                ])
            ])
        ])
    )

    print(valid_page)
    print("Valid page:", valid_page.is_valid())
    valid_page.write_to_file("valid_page.html")

    invalid_page = Page(
        Html([
            Body(),
            Head([
                Title(Text("Wrong order"))
            ])
        ])
    )

    print("Invalid page:", invalid_page.is_valid())

    invalid_table = Page(
        Table([
            Tr([
                Th(Text("Name")),
                Td(Text("Judith"))
            ])
        ])
    )

    print("Invalid table:", invalid_table.is_valid())


if __name__ == '__main__':
    try:
        test()
    except Exception as error:
        print(error)