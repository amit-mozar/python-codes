#method 1 - Extreme brute force -> O(n3)
nums = [1, 99, 101, 98, 2, 5, 3, 100]
max_length = 0
for num in nums:
    curr_num = num
    length = 1
    while True:
        found = False
        for j in range(len(nums)):
            if nums[j] == curr_num + 1:
                curr_num += 1
                length += 1
                found = True
                break
        if not found:
            break
        max_length = max(max_length, length)
print(max_length)

#method 2 - Better brute force -> O(n2)
max_length = 0
def contains(nums, target):
    for num in nums:
        if num == target:
            return True
    return False

for num in nums:
    curr_num = num
    length = 1
    while contains(nums, curr_num + 1):
        length+= 1
        curr_num += 1
    max_length = max(max_length, length)
print(max_length)