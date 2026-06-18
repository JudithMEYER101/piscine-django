def my_var():
    """Create many variables with different types
        then display each tipe at runtime"""

    a = 42                  #int
    b = "42"                #str    
    c = "quarante-deux"     #str
    d = 42.0                #float
    e = True                #bool
    f = [42]                #list
    g = {42: 42}            #dict
    h = (42,)               #tuple
    i = set()               #set

    variables = [a, b, c, d, e, f, g, h, i]

    for var in variables:
        print(var, "est de type", type(var))


if __name__ == '__main__':
    my_var()