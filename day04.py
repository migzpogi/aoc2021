class CardNumber:
    def __init__(self, idx, value):
        self.idx = idx
        self.value = value
        self.hit = False

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


def get_row_index():
    k = 0
    row_index = []
    for i in range(0, 5):
        temp = []
        for j in range(0, 5):
            temp.append(k)
            k += 1
        row_index.append(temp)

    return row_index


def get_col_index():
    col_index = []
    for i in range(0, 5):
        k = i
        temp = []
        for j in range(0, 5):
            temp.append(k)
            k += 5

        col_index.append(temp)

    return col_index


def create_card(numbers):
    card = []
    for idx, number in enumerate(numbers):
        card.append(CardNumber(idx, number))

    return card


def check_win(card):
    rows = get_row_index()
    cols = get_col_index()

    for row in rows:
        true_count = 0
        for r in row:
            if card[r].hit is True:
                true_count += 1
        if true_count == 5:
            return True

    for col in cols:
        true_count = 0
        for c in col:
            if card[c].hit is True:
                true_count += 1
        if true_count == 5:
            return True

    return False


# a = [14, 21, 17, 24, 4, 10, 16, 15, 9, 19, 18, 8, 23, 26, 20, 22, 11, 13, 6, 5, 2, 0, 12, 3, 7]
# c = create_card(a)
#
# c[0].hit = True
# c[5].hit = True
# c[10].hit = True
# c[15].hit = True
# c[20].hit = True
# c[18].hit = True
#
# print(check_win(c))

call_numbers = []
cards = []
temp = []
x = input_file_to_list("day04_input.txt")
for idx, line in enumerate(x):
    if idx == 0:
        called = line.split(',')
        for c in called:
            call_numbers.append(int(c))
    else:
        l = line.split(' ')
        if len(l) == 1:
            if temp:
                buffer = []
                for idx, t in enumerate(temp):
                    buffer.append(CardNumber(idx, int(t)))
                cards.append(buffer)
            temp = []
        else:
            for i in l:
                if i != '' and i != 'a':
                    temp.append(i)


def run():
    for called in call_numbers:
        for idx, card in enumerate(cards):
            for c in card:
                if c.value == called:
                    c.hit = True
            if check_win(card):
                print(f"Won in card {idx}, last called {called}")
                not_hit = 0
                for x in cards[idx]:
                    if x.hit == False:
                        not_hit += x.value

                print(f"Not hit {not_hit}")

                return

run()
