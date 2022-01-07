class LanternSchool:
    def __init__(self):
        self.fish_count = {}

    def add_fish(self, fish):
        if self.fish_count.get(fish):
            self.fish_count[fish] += 1
        else:
            self.fish_count[fish] = 1

    def next_day(self):
        temp = {}
        for fish in self.fish_count.items():
            state = fish[0]
            count = fish[1]

            if state == 0:
                if temp.get(6):
                    temp[6] += count
                else:
                    temp[6] = count

                if temp.get(8):
                    temp[8] += count
                else:
                    temp[8] = count
            else:
                state -= 1
                if temp.get(state):
                    temp[state] += count
                else:
                    temp[state] = count

        self.fish_count = temp

    def count_fish(self):
        return sum(self.fish_count.values())

    def days_elapsed(self, days):
        for i in range(0, days):
            self.next_day()
            # print(f'{i+1} - {self.count_fish()} - {self.fish_count}')





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
starting_fish = input_file_to_list("day06_input.txt")[0].split(',')
for fish in starting_fish:
    school.add_fish(int(fish))

school.days_elapsed(256)
print(school.count_fish())