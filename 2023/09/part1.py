with open('input.txt', 'r') as file:
    lines = [[int(num) for num in line.split(' ')] for line in file.read().splitlines()]

def get_differences(nums):
    return [num - nums[i] for i, num in enumerate(nums[1:])]

def predict_next(nums):
    if any(nums):
        return nums[-1] + predict_next(get_differences(nums))
    return 0

print(sum([predict_next(line) for line in lines]))