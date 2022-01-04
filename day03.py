print(int('10110', 2))  # 22


class DigitCount:
    def __init__(self, name):
        self.name = name
        self.one = 0
        self.zero = 0

    def most_common(self):
        if self.one == self.zero:
            return '1'
        elif self.one > self.zero:
            return '1'
        else:
            return '0'

    def least_common(self):
        if self.one == self.zero:
            return '0'
        elif self.one > self.zero:
            return '0'
        else:
            return '1'


class Report:
    def __init__(self):
        self.digits = []

    def get(self, name):
        for d in self.digits:
            if d.name == name:
                return d

    def increment_zero(self, name):
        for d in self.digits:
            if d.name == name:
                d.zero += 1

    def increment_one(self, name):
        for d in self.digits:
            if d.name == name:
                d.one += 1


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


# r = Report()
#
# for i in range(1, 13):
#     r.digits.append(DigitCount(i))
#
# bits = input_file_to_list("day03_input.txt")
# for i, bit in enumerate(bits):
#     for j, digit in enumerate(bit):
#         if int(digit) == 0:
#             r.increment_zero(j+1)
#         else:
#             r.increment_one(j+1)
#
# gamma = ""
# epsilon = ""
#
# for x in r.digits:
#     gamma += x.most_common()
#
# for x in gamma:
#     if x == '1':
#         epsilon += '0'
#     else:
#         epsilon += '1'
#
# print(gamma)
# g = (int(gamma, 2))
# print(epsilon)
# e = (int(epsilon, 2))
# print(g*e)



bits = input_file_to_list("day03_input.txt")
idx = 0
remaining = len(bits)
while remaining > 1:
    x_count = 0
    r = Report()
    for i in range(1, 13):
        r.digits.append(DigitCount(i))

    for bit in bits:
        if bit == 'x':
            continue

        if bit[idx] == '0':
            r.increment_zero(idx+1)
        else:
            r.increment_one(idx+1)

    most_common = r.get(idx+1).most_common()

    for i, j in enumerate(bits):
        if j == 'x':
            continue

        if j[idx] != most_common:
            bits[i] = 'x'
            x_count += 1

    remaining = remaining - x_count
    idx += 1

for i in bits:
    if i == 'x':
        continue
    else:
        print(i)
        print(int(i, 2))

bits = input_file_to_list("day03_input.txt")
idx = 0
remaining = len(bits)
while remaining > 1:
    x_count = 0
    r = Report()
    for i in range(1, 13):
        r.digits.append(DigitCount(i))

    for bit in bits:
        if bit == 'x':
            continue

        if bit[idx] == '0':
            r.increment_zero(idx+1)
        else:
            r.increment_one(idx+1)

    most_common = r.get(idx+1).least_common()

    for i, j in enumerate(bits):
        if j == 'x':
            continue

        if j[idx] != most_common:
            bits[i] = 'x'
            x_count += 1

    remaining = remaining - x_count
    idx += 1

for i in bits:
    if i == 'x':
        continue
    else:
        print(i)
        print(int(i, 2))
