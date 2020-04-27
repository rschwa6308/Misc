

def steps_to_wire_partial(steps):
    wire = [(0, 0)]
    x, y = 0, 0
    for (direction, count) in steps:
        if direction == "U":
            y += count
        elif direction == "D":
            y -= count
        elif direction == "L":
            x -= count
        elif direction == "R":
            x += count
        wire.append((x, y))
    return wire


# def wire_contains_point(wire, x, y):
#     for i in range(len(wire) - 1):
#         if wire[i][0] == wire[i + 1][0] and wire[i][0] == x:
#             if (wire[i][1] - y) * (wire[i + 1][1] - y) <= 0:
#                 return True
#         if wire[i][1] == wire[i + 1][1] and wire[i][1] == y:
#             if (wire[i][0] - x) * (wire[i + 1][0] - x) <= 0:
#                 return True
#     return False


def get_segment_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    x3, x4 = sorted([x3, x4])
    y3, y4 = sorted([y3, y4])

    vert_a = x1 == x2
    vert_b = x3 == x4

    if vert_a and vert_b:
        if x1 == x3:
            print("PARRALEL VERTICAL INTERSECTION!!!")

    if not vert_a and not vert_b:
        if y1 == y3:
            print(f"PARRALEL HORIZONTAL INTERSECTION!!! {x1, y1, x2, y2, x3, y3, x4, y4}")
    
    if vert_a:  # make a horizontal and b vertical
        x1, y1, x2, y2, x3, y3, x4, y4 = x3, y3, x4, y4, x1, y1, x2, y2
    
    if y3 <= y1 <= y4 and x1 <= x3 <= x2:
        return (x3, y1)
    


def get_points_at_distance(dist):
    points = []
    points += [(dist - i, i) for i in range(dist)]
    points += [(-i, dist - i) for i in range(dist)]
    points += [(-dist + i, -i) for i in range(dist)]
    points += [(i, -dist + i) for i in range(dist)]
    return points


if __name__ == "__main__":
    a_steps, b_steps = [
        [(step[0], int(step[1:])) for step in wire.strip().split(",")]
        for wire in open("Day 3 input.txt").read().split("\n")
    ]

    a_wire, b_wire = steps_to_wire_partial(a_steps), steps_to_wire_partial(b_steps)

    intersections = []
    for i in range(len(a_wire) - 1):
        for j in range(len(b_wire) - 1):
            res = get_segment_intersection(
                *a_wire[i], *a_wire[i + 1],
                *b_wire[j], *b_wire[j + 1]
            )
            if res is not None and res != (0, 0):
                print(f"Intersection found!: {res}")
                intersections.append(res)

    print(min([abs(x) + abs(y) for (x, y) in intersections]))
