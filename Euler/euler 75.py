from math import gcd


p_limit = 1500000

m_limit = int((p_limit / 2) ** 0.5)
triangles = [0] * (p_limit + 1)
for m in range(2, m_limit + 1):
    for n in range(1, m):
        if (n + m) % 2 == 0 or gcd(m, n) > 1:
            continue
        a = m * m + n * n
        b = m * m - n * n
        c = 2 * m * n
        # print(a, b, c)
        p = a + b + c
        i = 1
        while p * i <= p_limit: 
            triangles[p * i] += 1
            i += 1

total = 0
for tri in triangles:
    if tri == 1:
        total += 1
print(total)

