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
    # indices, not low points
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


def get_sides(len, wid):
    # indices, not low points
    up = list(range(1, len-1))
    left = list(range(len, len*(int((wid*len)/len)-1), len))
    right = list(range(len+(len-1), len*(int((wid*len)/len)-1)+(len-1), len))
    down = list(range(((len*wid)-len)+1, (len*wid)-1))
    return (up, left, right, down)


def get_sides_adj(points, idx, loc, len):
    low_points_idx = []
    if loc == 'top':
        for p in idx:
            left = points[p-1]
            right = points[p+1]
            bottom = points[p+len]

            if points[p] < left and points[p] < right and points[p] < bottom:
                low_points_idx.append(p)

    return low_points_idx



def run_sides(points, len, wid):
    low_points_idx = []
    sides_idx = get_sides(len, wid)

    top_lowpoints = get_sides_adj(points, sides_idx[0], 'top', len)
    low_points_idx.extend(top_lowpoints)

    return low_points_idx


points = create_long_list("sample.txt")

idx_corners = get_corners(10, 5)  # indices of corners
idx_sides = get_sides(10, 5)  # indices of sides
print(idx_corners)
print(idx_sides)

low_corners = run_corners(points, 10, 5)
print(low_corners)  # low points index, corners

low_sides = run_sides(points, 10, 5)
print(low_sides) # low points index, sides



# points = create_long_list("day09_input.txt")
# print(get_corners(100, 100))
# print(points[0], points[99], points[9900], points[9999])
# print(get_corners_adj(points, 0, 'ul', 100))