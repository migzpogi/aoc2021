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


def get_corners_adj(points, idx, loc, len):
    beside = 0
    across = 0

    if loc == 0:
        beside = idx+1
        across = idx+len
    if loc == 1:
        beside = idx-1
        across = idx+len
    if loc == 2:
        beside = idx+1
        across = idx-len
    if loc == 3:
        beside = idx-1
        across = idx-len

    if points[idx] < points[beside] and points[idx] < points[across]:
        return True
    else:
        return False

def run_corners(points, len, wid):
    low_points_idx = []
    corners_idx = get_corners(len, wid)

    for idx, i in enumerate(corners_idx):
        if get_corners_adj(points, i, idx, len):
            low_points_idx.append(i)

    return low_points_idx



points = create_long_list("sample.txt")
corners = run_corners(points, 10, 5)

# points = create_long_list("day09_input.txt")
# print(get_corners(100, 100))
# print(points[0], points[99], points[9900], points[9999])
# print(get_corners_adj(points, 0, 'ul', 100))