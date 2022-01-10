class CrabSubs:
    def __init__(self, list_of_positions):
        self.crab_positions = {}
        self.max_pos = max(list_of_positions)
        self.min_pos = min(list_of_positions)

        for position in list_of_positions:
            self.add_crab(position)

    def add_crab(self, position):
        if self.crab_positions.get(position):
            self.crab_positions[position] += 1
        else:
            self.crab_positions[position] = 1

    def get_total_fuel_in_pos(self, position):
        total_fuel = 0
        for crab in self.crab_positions.items():
            total_fuel += abs(crab[0] - position) * crab[1]

        return total_fuel


def input_file_to_list(file_path):
    """
    Opens the input file for the problem and store line by line contents in a list
    :param file_path:
    :return:
    """
    file_contents = []
    with open(file_path, "r+") as f:
        for line in f.readlines():
            file_contents.append(line.strip())

    return file_contents


crab_positions = input_file_to_list("sample.txt")
crabs = CrabSubs(list(map(lambda x: int(x), crab_positions[0].split(','))))
print(crabs.crab_positions)
print(crabs.max_pos)
print(crabs.min_pos)
print(crabs.get_total_fuel_in_pos(3))