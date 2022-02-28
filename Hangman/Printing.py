import textwrap

def get_boxed(contents, width=50):
    tl, tr, bl, br, vert, hor = "┌┐└┘│─"

    out = ""

    lines = contents.split("\n")

    if any(len(line) > width for line in lines):
        raise ValueError(f"contents is too wide to fit in box of width {width}")

    out += tl + hor * (width + 2) + tr + "\n"
    for line in lines:
        out += f"{vert} {line:<{width}} {vert}\n"
    out += bl + hor * (width + 2) + br + "\n"

    return out



GALLOWS = """\
  ┌───┐
  │   O
  │   │
  │  ╱
──┴──\
"""


def print_game(board, incorrect_guesses, width=50):
    gallows = GALLOWS

    w, h = 5, 2
    word_grid = [[" " for _ in range(w)] for _ in range(h)]
    for i, c in enumerate(incorrect_guesses):
        word_grid[i//w][i%w] = c
    word_box = get_boxed(
        "\n".join(" ".join(row) for row in word_grid),
        width=w*2-1
    )

    board_str = " ".join(" " if b is None else b for b in board) + "\n" +\
                " ".join("‾" for _ in board)

    out = ""
    g_width = max(len(l) for l in gallows.split("\n"))
    out += "\n".join(
        f"{a:<{g_width}}{b:>{width-g_width}}"
        for a, b in zip(gallows.split("\n"), word_box.split("\n"))
    )

    out += "\n\n"

    out += "\n".join(
        f"{line:^{width}}"
        for line in board_str.split("\n")
    )
    
    # print(out)
    print(get_boxed(out, width=width))


    # contents = "X\nX\nX\n" +\
    #     ' '.join('_' if b is None else b for b in board)
    # print_boxed(contents)


if __name__ == "__main__":
    print_game(
        [None, "A", None, "B", None, "C", "D", "E"],
        ["X", "Y", "Z", "Q", "W", "L"]
    )