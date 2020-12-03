def main():
    with open("input.txt") as f:
        content = f.readlines()
        entries = [x.strip() for x in content]
    
    planets_dict = {}
    planets_dict["COM"] = Node("COM", None)

    for entry in entries:
        planets = read_entry(entry)

        planets_dict[planets[1]] = Node(planets[1], planets[0])

    total_distance = 0

    for planet in planets_dict:
        curr_planet = planets_dict[planet]

        while curr_planet.next_ != None:
            curr_planet = planets_dict[planets_dict[curr_planet.next_].name]
            total_distance += 1

    print(total_distance)

def read_entry(entry):
    return entry.split(")")


class Node():

    def __init__(self, name, next_):
        self.name = name
        self.next_ = next_

main()