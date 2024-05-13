def can_jump(nums):
    target = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] <= target:
            target = i
    return target == 0

if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print("Can Jump to the Last Index:", can_jump(nums))
