def print_possessive_names(data):
    for row in data:
        name = row[0]

        # Check if the name ends with 's' and adjust the possessive form accordingly
        if name[-1] == 's':
            possessive_name = name + "'"
        else:
            possessive_name = name + "'s"

        print(possessive_name)

names = [
    ["John", 25, "Male"],
    ["Sarah", 30, "Female"],
    ["Michael", 22, "Male"],
    ["Ryan", 35, "male"],
    ["Jessica", 25, "female"],
    ["samantha", 48, "female"],
]

print_possessive_names(names)
