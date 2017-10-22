from pprint import pprint


# def pascal(n):
#     if n == 1:
#         return [1]
#     else:
#         line = [1]
#         previous_line = pascal(n-1)
#         for i in range(len(previous_line) - 1):
#             line.append(previous_line[i] + previous_line[i + 1])
#         line += [1]
#     return line


# def pascal_prime(n):
#   p = pascal(n)
#   return [p[k + 1] / p[k] for k in range(n - 1)]



rows = 100


def relation(a, b):
  return a + b


pascal = [[1]]
for n in range(1, rows):
  previous_line = pascal[n - 1]
  line = []
  line.append(1)
  for k in range(1, n - 1):
    line.append(relation(previous_line[k - 1], previous_line[k]))
  line.append(1)
  pascal.append(line)


pascal_prime_row_sums = []
for n in range(rows):
  p = pascal[n]
  pascal_prime_n = [p[k + 1] / p[k] for k in range(n - 1)]
  pascal_prime_row_sums.append(sum(pascal_prime_n))


print([i for i in enumerate(pascal_prime_row_sums)])
