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

horizontal_pos = 0
vertical_pos = 0

steps = input_file_to_list("day02_input.txt")
# steps = input_file_to_list("sample.txt")
for step in steps:
    instruction = step.split(' ')
    move = instruction[0]
    unit = int(instruction[1])
    if move == 'forward':
        horizontal_pos += unit
    if move == 'down':
        vertical_pos += unit
    if move == 'up':
        vertical_pos -= unit

print(horizontal_pos * vertical_pos)