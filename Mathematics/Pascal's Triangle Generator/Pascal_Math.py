def get_triangle(rule, rows, base=1, surrounding=0):
    pascal = [[base]]
    for n in range(1, rows):
        previous_line = pascal[n - 1]
        line = []
        line.append(rule(surrounding, previous_line[0]))
        for k in range(1, n):
            line.append(rule(previous_line[k - 1], previous_line[k]))
        line.append(rule(previous_line[-1], surrounding))
        pascal.append(line)

    return pascal


def get_printable_triangle(tri, lens=None):
    str = ""

    rows = len(tri)

    if not lens:
        lens = lambda num: str(num)

    for n in range(rows):
        spacing = " " * (rows - n)
        data = " ".join([lens(num) for num in tri[n]])
        str += spacing + data + "\n"

    return str


def print_triangle(tri, lens=None):
    str = get_printable_triangle(tri, lens)
    print(str)