def shortest_path_squared(w, l, h):
    # assumes dimensions given in ascending order
    return (w + l) ** 2 + h ** 2
        

def is_perfect_square(n, epsilon=1e-9):
    s = n ** 0.5
    return s - int(s) < epsilon



# Naive Approach
# count = 0
# M = 1000
# for w in range(1, M + 1):
#     for l in range(w, M + 1):
#         for h in range(l, M + 1):
#             p = shortest_path_squared(w, l, h)
#             if is_perfect_square(p):
#                 count += 1



def f(M):
    count = 0
    for h in range(2, M + 1):
        # find all pythagorean triples of the form (h, wl, ...) s.t. wl < 2h
        # each one contributes a (combinatorially simple) number of unique cuboids
        for wl in range(2, 2*h):
            if is_perfect_square(h**2 + wl**2):
                if wl > h:
                    count += (h - (wl - h)) // 2
                else:
                    count += wl // 2 + 1
    return count


def binary_search(func, target, low, high):
    print(low, high)
    mid = (low + high) // 2
    val = func(mid)
    print(val)
    if val == target or high - low == 1:
        return mid

    if val < target:
        low = mid + 1
    else:
        high = mid
    
    return binary_search(func, target, low, high)


print(binary_search(f, 1_000_000, 1500, 2000) + 2)
# -> 1818
