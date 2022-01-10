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

    def get_triangle_fuel(self, position):
        total_fuel = 0
        for crab in self.crab_positions.items():
            n = abs(crab[0] - position)
            triangle = ((n**2) + n)/2
            total_fuel += triangle * crab[1]

        return total_fuel

    def least_fuel(self):
        fuels = {}
        for i in range(self.min_pos, self.max_pos+1):
            fuel = self.get_total_fuel_in_pos(i)
            if fuels.get(fuel):
                pass
            else:
                fuels[fuel] = i

        # return fuels[min(fuels)]
        return min(fuels)

    def least_triangle_fuel(self):
        fuels = {}
        for i in range(self.min_pos, self.max_pos+1):
            fuel = self.get_triangle_fuel(i)
            if fuels.get(fuel):
                pass
            else:
                fuels[fuel] = i

        # return fuels[min(fuels)]
        return min(fuels)


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


crab_positions = input_file_to_list("day07_input.txt")
crabs = CrabSubs(list(map(lambda x: int(x), crab_positions[0].split(','))))
print(crabs.least_fuel())
print(crabs.least_triangle_fuel())