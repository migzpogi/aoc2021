class Coordinates:
    def __init__(self, coords):
        self.coords = coords
        self.point_1 = self.coords[0]
        self.point_2 = self.coords[1]
        self.x1 = int(self.point_1.split(',')[0])
        self.y1 = int(self.point_1.split(',')[1])
        self.x2 = int(self.point_2.split(',')[0])
        self.y2 = int(self.point_2.split(',')[1])
        self.orientation = self.__get_orientation()

    def __get_orientation(self):
        if self.x1 == self.x2:
            if self.y2 > self.y1:
                return "vi"
            else:
                return "vd"
        if self.y1 == self.y2:
            if self.x2 > self.x1:
                return "hi"
            else:
                return "hd"

    def points_in_between(self):
        points = []
        if self.orientation == 'vi':
            for i in range(self.y1, self.y2+1):
                points.append((self.x1, i))
        if self.orientation == 'vd':
            for i in range(self.y1, self.y2-1, -1):
                points.append((self.x1, i))
        if self.orientation == 'hi':
            for i in range(self.x1, self.x2+1):
                points.append((i, self.y1))
        if self.orientation == 'hd':
            for i in range(self.x1, self.x2-1, -1):
                points.append((i, self.y1))

        return points


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


def list_points_between_coordinates(coords):
    """
    Lists the points that fall under the given coordinates
    :param coords: tuple of coordinates ('x1,y1', 'x2,y2')
    :return:
    """

    c = Coordinates(coords)
    return c.points_in_between()

point_count = {}
coords = get_coordinates_from_file("day05_input.txt")
for coord in coords:
    for point in list_points_between_coordinates(coord):
        if point_count.get(point):
            point_count[point] += 1
        else:
            point_count[point] = 1

intersect = 0
for p in point_count.items():
    if(p[1]) > 1:
        intersect += 1

print(intersect)

