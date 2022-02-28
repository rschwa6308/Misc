a, b = 1, 1

a_end = 1
b_end = 1

a_start = 1
b_start = 1


def pandigital(n_str):
    return all(i in n_str for i in "123456789")


# print(pandigital("123456789"))


# def small(n):
#     return int(str(n))


buffer = 1000


for k in range(1, 100_000_000):
    if k % 1_000_000 == 0: print(f"progress: {k}")
    if pandigital(str(b_start)[:9]) and pandigital(str(b_start)[-9:]):
        print(k)

    # if pandigital(n_str):
    #     print(k)

    # a, b = a + b, a

    a_end, b_end = a_end + b_end, a_end
    a_end = a_end % 10**9
    b_end = b_end % 10**9
    # a = small(a)
    # b = small(b)

    a_start, b_start = a_start + b_start, a_start
    z = max(0, min(len(str(a_start)), len(str(b_start))) - (9 + buffer))
    a_start //= 10**z
    b_start //= 10**z
    # print(b, b_start, z)

    # print(len(str(b)), len(str(b_start)))

    # assert(str(b)[:9] == str(int(b_start))[:9])
    # assert(int(str(b)[-9:]) == int(str(int(b_end))[-9:]))

