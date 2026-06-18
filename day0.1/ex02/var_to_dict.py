def musicians_to_dict():
    """Create a dict with date as key and
        musician as name as var then display"""

    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]

    result = {}

    #Create key + var, if we have the same date many times we add the name
    #to the key (can't have same key multiple time in dict)
    for name, year in d:
        if year not in result:
            result[year] = name
        else:
            result[year] += " " + name

    for year in result:
        print(year, ":", result[year])

    #Result won't be ordered because dict is key based lookup not ordered list

if __name__ == '__main__':
    musicians_to_dict()