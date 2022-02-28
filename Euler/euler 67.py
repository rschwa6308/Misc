with open('p067_triangle.txt') as f:
    triangle = [
        [int(n) for n in line.split(' ')]
        for line in f.readlines()
    ]

for y in range(99, 0, -1):
    for x in range(y):
        triangle[y - 1][x] += max(triangle[y][x], triangle[y][x + 1])

print(triangle[0][0])