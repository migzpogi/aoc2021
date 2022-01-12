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


def create_long_list(file_path):
    points = input_file_to_list(file_path)
    list_of_points = []
    for point in points:
        for p in point:
            list_of_points.append(p)

    return list_of_points


def get_corners(len, wid):
    upper_left = 0
    upper_right = len-1
    lower_left = len * (wid - 1)
    lower_right = (len * wid) - 1

    return upper_left, upper_right, lower_left, lower_right


points = create_long_list("day09_input.txt")
# print(points)
print(get_corners(100, 100))
print(points[0], points[99], points[9900], points[9999])