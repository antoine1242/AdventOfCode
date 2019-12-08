def main():
    with open("input.txt") as f:
        content = f.readlines()
        entries = [x.strip() for x in content]
    
    planets_dict = {}
    planets_dict["COM"] = Node("COM", None)

    for entry in entries:
        planets = read_entry(entry)

        planets_dict[planets[1]] = Node(planets[1], planets[0])

    you = planets_dict["YOU"]
    san = planets_dict["SAN"]

    planets_list_you = []

    while you.next_ != None:
        planets_list_you.append(you.next_)
        you = planets_dict[you.next_]

    planets_list_san = []

    while san.next_ != None:
        planets_list_san.append(san.next_)
        san = planets_dict[san.next_]

    first_common_planet = get_first_common_element(planets_list_you, planets_list_san)

    indx1 = planets_list_you.index(first_common_planet)
    indx2 = planets_list_san.index(first_common_planet)

    print(indx1 + indx2)

def get_first_common_element(x,y):
    for i in x:
        if i in y:
            return i

def read_entry(entry):
    return entry.split(")")


class Node():

    def __init__(self, name, next_):
        self.name = name
        self.next_ = next_

main()