


def cross_product_2d(A, B):
    return A[0]*B[1] - A[1]*B[0]




# def sgn(x):
#     return -1 if x < 0 else 1



def point_left_of_line(a, b, p):
    ab = (b[0] - a[0], b[1] - a[1])
    ap = (p[0] - a[0], p[1] - a[1])
    
    return cross_product_2d(ab, ap) > 0



# print(point_left_of_line((-5, -5), (1, 5), (0, 0)))



def triangle_contains_origin(a, b, c):
    o = (0, 0)
    return all([
        point_left_of_line(a, b, o) == point_left_of_line(a, b, c),
        point_left_of_line(a, c, o) == point_left_of_line(a, c, b),
        point_left_of_line(b, c, o) == point_left_of_line(b, c, a),
    ])



# print(triangle_contains_origin((-340,495), (-153,-910), (835,-947)))
# print(triangle_contains_origin((-175,41), (-421,-714), (574,-645)))


triangles = []
with open("p102_triangles.txt") as f:
    for line in f.readlines():
        nums = [int(n) for n in line.split(",")]
        triangles.append(list(zip(nums[::2], nums[1::2])))


print(triangles[0])



count = 0
for a, b, c in triangles:
    if triangle_contains_origin(a, b, c):
        count += 1


print(count)