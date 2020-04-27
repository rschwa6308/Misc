from Day_2_A import run_program


if __name__ == "__main__":
    nums = list(map(int, open("Day 2 input.txt").read().split(",")))

    for noun in range(100):
        for verb in range(100):
            nums_copy = list(nums)
            nums_copy[1], nums_copy[2] = noun, verb
            if run_program(nums_copy) == 19690720:
                print(noun * 100 + verb)