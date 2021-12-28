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


def sum_of_sliding_three_measurements(list_of_depths):
    """
    Gets the sum of a three-measurement sliding window
    :param list_of_depths:
    :return:
    """
    sum_of_slides = []
    slide_size = 3
    depths = list(map(lambda x: int(x), list_of_depths))  # convert elements to int

    for i in range(len(depths) - slide_size + 1):
        sum_of_slides.append(sum(depths[i: i+slide_size]))

    return count_increased(sum_of_slides)



measurements = input_file_to_list("day01_input.txt")
print(count_increased(measurements))
print(sum_of_sliding_three_measurements(measurements))