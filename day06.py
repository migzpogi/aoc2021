class LanternSchool:
    def __init__(self):
        self.fishes = []

    def add_fish_to_school(self, fish):
        self.fishes.append(fish)

    def create_fish(self, state):
        fish = LanternFish(state)
        self.add_fish_to_school(fish)

    def show_fish_states(self):
        for fish in self.fishes:
            print(fish.state)

    def next_day(self):
        for fish in self.fishes:
            if fish.state == 0:
                self.create_fish(9)
                fish.state = 7
            fish.next_day_state()

    def days_elapsed(self, days):
        for i in range(0, days):
            if i%20 == 0:
                print(f"Day {i}")
            self.next_day()

    def fish_count(self):
        return len(self.fishes)


class LanternFish(LanternSchool):
    def __init__(self, state):
        super().__init__()
        self.state = state

    def next_day_state(self):
        self.state -= 1

    def set_state_after_elapsed_days(self, days):
        for i in range(1, days+1):
            self.state -= 1
            if self.state == -1:
                self.state = 6
        return self.state

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

school = LanternSchool()
starting_fish = input_file_to_list("sample.txt")[0].split(',')
for fish in starting_fish:
    school.create_fish(int(fish))

school.days_elapsed(180)
print(school.fish_count())
