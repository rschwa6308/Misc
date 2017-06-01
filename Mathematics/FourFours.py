from pprint import pprint

from Operations import *


def get_all_configs(A, B, C):
    atom = 4
    all_configs = [
        A([B([C([atom, atom]), atom]), atom]),
        A([B([atom, C([atom, atom])]), atom]),
        A([B([atom, atom]), C([atom, atom])]),
        A([atom, B([C([atom, atom]), atom])]),
        A([atom, B([atom, C([atom, atom])])])
    ]
    return all_configs


def main():
    solved = []
    count = 0

    for A in op_set:
        for B in op_set:
            for C in op_set:
                for expression in get_all_configs(A, B, C):
                    count += 1
                    value = expression.evaluate()
                    print(expression.to_string(), " = ", value)
                    if value is not None and value == int(value) and value >= 0 and value not in solved:
                        solved.append(int(value))

    print(sorted(solved))
    # print(len(solved), " / ", count)

    print("Missing from first 30: ", [n for n in range(30) if n not in solved])




if __name__ == "__main__":
    main()
