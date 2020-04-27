def run_program(nums):
    index = 0
    while nums[index] != 99:
        if nums[index] == 1:
            nums[nums[index + 3]] = nums[nums[index + 1]] + nums[nums[index + 2]]
        else:
            nums[nums[index + 3]] = nums[nums[index + 1]] * nums[nums[index + 2]]
        index += 4

    return nums[0]


if __name__ == "__main__":
    nums = list(map(int, open("Day 2 input.txt").read().split(",")))
    nums[1], nums[2] = 12, 2
    print(run_program(nums))