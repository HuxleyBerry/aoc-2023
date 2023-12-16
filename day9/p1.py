def find_differences(nums):
    all_zeroes = True
    differences = []
    for i in range(len(nums)-1):
        diff = nums[i+1] - nums[i]
        if diff != 0:
            all_zeroes = False
        differences.append(diff)
    if all_zeroes:
        return [0]
    else:
        child_final_differences = find_differences(differences)
        child_final_differences.append(differences[0])
        return child_final_differences
        
    

def find_next(nums):
    start = 0
    for diff in find_differences(nums)[1:]:
        start = diff - start
    return nums[0] - start

with open("input.txt") as file:
    _sum = 0
    for line in file:
        nums = [int(n) for n in line.strip().split()]
        _sum += find_next(nums)
    print(_sum)
    