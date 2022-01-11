class Segment:
    def __init__(self, code):
        self.code = code
        self.pattern = []
        self.output = []

        self.__init_pattern()
        self.__init_output()

    def __init_pattern(self):
        for pattern in self.code.split('|')[0].split(' '):
            if pattern != '':
                # self.pattern.append(pattern)
                self.pattern.append(self.__sort(pattern))

    def __init_output(self):
        for output in self.code.split('|')[1].split(' '):
            if output != '':
                # self.output.append(output)
                self.output.append(self.__sort(output))

    def __sort(self, str):
        return "".join(sorted(str))

    def are_unique_present(self):
        unique = ""
        for pattern in self.pattern:
            if len(pattern) == 2:
                unique += '1'
            if len(pattern) == 3:
                unique += '7'
            if len(pattern) == 4:
                unique += '4'
            if len(pattern) == 7:
                unique += '8'

        return unique

    def count_1478_output(self):
        unique_len = [2, 3, 4, 7]
        sum = 0
        for output in self.output:
            if len(output) in unique_len:
                sum += 1

        return sum

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


codes = input_file_to_list("day08_input.txt")
output_total = 0
for code in codes:
    segment = Segment(code)
    output_total += segment.count_1478_output()

print(output_total)