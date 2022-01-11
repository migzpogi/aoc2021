class Segment:
    def __init__(self, code):
        self.code = code
        self.pattern = []
        self.output = []

        self.up = ""
        self.mid = ""
        self.down = ""
        self.ur = ""
        self.dr = ""
        self.ul = ""
        self.dl = ""

        self.digit_0_pattern = ""
        self.digit_1_pattern = ""
        self.digit_2_pattern = ""
        self.digit_3_pattern = ""
        self.digit_4_pattern = ""
        self.digit_5_pattern = ""
        self.digit_6_pattern = ""
        self.digit_7_pattern = ""
        self.digit_8_pattern = ""
        self.digit_9_pattern = ""

        self.done_pattern  = []

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

    def find_digit_1(self):
        for pattern in self.pattern:
            if len(pattern) == 2 and pattern not in self.done_pattern:
                self.digit_1_pattern = pattern
                self.done_pattern.append(pattern)
                self.ur = pattern
                self.dr = pattern

    def find_digit_7(self):
        for pattern in self.pattern:
            if len(pattern) == 3 and pattern not in self.done_pattern:
                self.digit_7_pattern = pattern
                self.done_pattern.append(pattern)
                self.up = self.get_difference(pattern, self.ur)[0]

    def find_digit_4(self):
        for pattern in self.pattern:
            if len(pattern) == 4 and pattern not in self.done_pattern:
                self.digit_4_pattern = pattern
                self.done_pattern.append(pattern)
                self.ul = "".join(self.get_difference(pattern, self.ur))
                self.mid = "".join(self.get_difference(pattern, self.ur))

    def find_digit_8(self):
        for pattern in self.pattern:
            if len(pattern) == 7 and pattern not in self.done_pattern:
                self.digit_8_pattern = pattern
                self.done_pattern.append(pattern)
                x = "".join(sorted(self.ur + self.up + self.ul))
                self.dl = "".join(self.get_difference(pattern, x))
                self.down = "".join(self.get_difference(pattern, x))

    def find_digit_3(self):
        for pattern in self.pattern:
            if len(pattern) == 5 and pattern not in self.done_pattern:
                x = "".join(sorted(self.ur + self.up))
                diff = "".join(self.get_difference(pattern, x))
                if len(diff) == 2:
                    self.digit_3_pattern = pattern
                    self.done_pattern.append(pattern)
                    self.mid = "".join(self.get_common(diff, self.mid))
                    self.down = "".join(self.get_common(diff, self.down))

                    self.ul = "".join(self.get_difference(self.mid, self.ul))
                    self.dl = "".join(self.get_difference(self.down, self.dl))
                    return

    def find_digit_5(self):
        for pattern in self.pattern:
            if len(pattern) == 5 and pattern not in self.done_pattern:
                x = "".join(sorted(self.ur + self.up))
                diff = "".join(self.get_difference(pattern, x))
                if len(diff) != 2:
                    a = "".join(self.get_common(pattern, self.ul))
                    if a == self.ul:
                        self.digit_5_pattern = pattern
                        self.done_pattern.append(pattern)
                        b = "".join(self.get_common(pattern, self.dr))
                        self.dr = b
                    # else:
                    #     self.digit_2_pattern = ""
                    #     b = "".join(self.get_common(pattern, self.ur))
                    #     self.ur = b

    def find_digit_2(self):
        for pattern in self.pattern:
            if len(pattern) == 5 and pattern not in self.done_pattern:
                x = "".join(sorted(self.ur + self.up))
                diff = "".join(self.get_difference(pattern, x))
                if len(diff) != 2:
                    a = "".join(self.get_common(pattern, self.ul))
                    if a != self.ul:
                        self.digit_2_pattern = pattern
                        self.done_pattern.append(pattern)
                        b = "".join(self.get_common(pattern, self.ur))
                        self.ur = b


    def find_digit_0(self):
        for pattern in self.pattern:
            if len(pattern) == 6 and pattern not in self.done_pattern:
                expected = "".join(sorted(self.ur + self.dr + self.down + self.dl + self.ul + self.up))
                if pattern == expected:
                    self.digit_0_pattern = pattern
                    self.done_pattern.append(pattern)

    def find_digit_6(self):
        for pattern in self.pattern:
            if len(pattern) == 6 and pattern not in self.done_pattern:
                expected = "".join(sorted(self.up + self.ul + self.dl + self.down + self.dr + self.mid))
                if pattern == expected:
                    self.digit_6_pattern = pattern
                    self.done_pattern.append(pattern)

    def find_digit_9(self):
        for pattern in self.pattern:
            if len(pattern) == 6 and pattern not in self.done_pattern:
                expected = "".join(sorted(self.up + self.ul + self.mid + self.ur + self.dr + self.down))
                if pattern == expected:
                    self.digit_9_pattern = pattern
                    self.done_pattern.append(pattern)


    def get_digits_from_pattern(self):
        self.find_digit_1()
        self.find_digit_7()
        self.find_digit_4()
        self.find_digit_8()

        self.find_digit_3()
        self.find_digit_5()
        self.find_digit_2()

        self.find_digit_0()
        self.find_digit_6()
        self.find_digit_9()


    def get_difference(self, str1, str2):
        first_set = set(str1)
        second_set = set(str2)
        diff = first_set.symmetric_difference(second_set)
        return sorted(list(diff))

    def get_common(self, str1, str2):
        return sorted(list(set(str1)&set(str2)))

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

    def output_to_digits(self):
        digits = ""
        for output in self.output:
            if output == self.digit_0_pattern:
                digits += '0'
            if output == self.digit_1_pattern:
                digits += '1'
            if output == self.digit_2_pattern:
                digits += '2'
            if output == self.digit_3_pattern:
                digits += '3'
            if output == self.digit_4_pattern:
                digits += '4'
            if output == self.digit_5_pattern:
                digits += '5'
            if output == self.digit_6_pattern:
                digits += '6'
            if output == self.digit_7_pattern:
                digits += '7'
            if output == self.digit_8_pattern:
                digits += '8'
            if output == self.digit_9_pattern:
                digits += '9'

        return digits

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
sum_output = 0
for code in codes:
    segment = Segment(code)
    # print(segment.pattern, segment.output)
    segment.get_digits_from_pattern()
    # print(f'0: {segment.digit_0_pattern}, '
    #       f'1: {segment.digit_1_pattern}, '
    #       f'2: {segment.digit_2_pattern}, '
    #       f'3: {segment.digit_3_pattern}, '
    #       f'4: {segment.digit_4_pattern}, '
    #       f'5: {segment.digit_5_pattern}, '
    #       f'6: {segment.digit_6_pattern}, '
    #       f'7: {segment.digit_7_pattern}, '
    #       f'8: {segment.digit_8_pattern}, '
    #       f'9: {segment.digit_9_pattern}')
    # print(segment.ur, segment.dr, segment.up, segment.ul, segment.mid, segment.dl, segment.down)
    # print(segment.output_to_digits())
    # print('---')
    sum_output += int(segment.output_to_digits())

print(sum_output)

