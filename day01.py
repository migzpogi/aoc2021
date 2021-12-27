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


def count_increased(list_of_depths):
    """
    Counts the number of times a depth measurement increased
    :param list_of_depths: retrieved from input file
    :return:
    """
    depths = list(map(lambda x: int(x), list_of_depths))  # convert elements to int

    previous = None
    increased_count = 0
    for depth in depths:
        if previous is None:
            previous = depth
        if depth > previous:
            increased_count += 1
        previous = depth

    return increased_count


print(count_increased(input_file_to_list("day01_input.txt")))