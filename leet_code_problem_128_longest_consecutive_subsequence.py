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
