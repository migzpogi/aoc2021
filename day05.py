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


def get_coordinates_from_file(file_path):
    """
    Transforms the input file into a tuple of coordinates
    :return:
    """
    list_of_coordinates = []
    input_file = input_file_to_list(file_path)
    for lines in input_file:
        coords = lines.split(' -> ')
        list_of_coordinates.append((coords[0], coords[1]))

    return list_of_coordinates

get_coordinates_from_file("sample.txt")
