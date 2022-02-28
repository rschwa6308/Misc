mat = []

with open("p081_matrix.txt") as f:
    for line in f.readlines():
        row = []
        for n in line.split(","):
            row.append(int(n))
        mat.append(row)

min_mat = [[None for _ in range(80)] for _ in range(80)]
min_mat[0][0] = mat[0][0]

def min_path(x, y):
    if x < 0 or y < 0:
        return 10000000000000
    
    if min_mat[y][x] is not None:
        return min_mat[y][x]
    
    val = min(
        min_path(x - 1, y),
        min_path(x, y - 1)
    ) + mat[y][x]

    min_mat[y][x] = val
    return val



print(min_path(79, 79))