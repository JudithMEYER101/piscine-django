def my_sort():
    """Sort a list from a dict using multy-key sorting (year, then alphabetical)"""

    d = {
        'Hendrix': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Beck': '1944',
        'Santana': '1947',
        'Ramone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939',
    }

    #transform keys and values into tuples
    #key->value becomes ("key, "value")
    #key=lambda item: (item[1], item[0]) makes it ("value", "key")
    #so we sort by year first then by alphabetical
    sorted_items = sorted(d.items(), key=lambda item: (int(item[1]), item[0]))

    for name, year in sorted_items:
        print(name)


if __name__ == '__main__':
    my_sort()