
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


def print_triangle(tri, lens=None):
    rows = len(tri)

    if not lens:
        lens = lambda num: str(num)

    for n in range(rows):
        spacing = " " * (rows - n)
        data = " ".join([lens(num) for num in tri[n]])
        print(spacing + data)


if __name__ == "__main__":
    from pprint import pprint

    # rule = lambda a, b: a ^ b
    # tri = get_triangle(rule, 64)
    #
    # lens = lambda num: "." if num else " "
    # print_triangle(tri, lens)

    # rule = lambda a, b: a + b
    # tri = get_triangle(rule, 64)
    #
    # lens = lambda num: "." if num % 2 else " "
    # print_triangle(tri, lens)

    rule = lambda a, b: a + b
    tri = get_triangle(rule, 10, base=1, surrounding=0)

    print_triangle(tri)
