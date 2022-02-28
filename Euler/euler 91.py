

def L2_sq(x, y):
    return x ** 2 + y ** 2


def is_right_triangle(x1, y1, x2, y2):
    a2, b2, c2 = sorted([
        L2_sq(x1, y1),
        L2_sq(x2, y2),
        L2_sq(x2 - x1, y2 - y1)
    ])
    return a2 != 0 and b2 != 0 and c2 != 0 and a2 + b2 == c2



M = 50

count = 0
for x1 in range(M+1):
    for y1 in range(M+1):
        for x2 in range(M+1):
            for y2 in range(M+1):
                if is_right_triangle(x1, y1, x2, y2):
                    # print((x1, y1), (x2, y2))
                    count += 1

print(count//2)     # double counting lol
# 14234