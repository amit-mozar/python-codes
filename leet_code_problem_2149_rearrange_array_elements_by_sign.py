#method 1 - brute force -> TC = O(n(n-1)/2) ~ O(n2); SC = O(n)
nums =[5, 10, -3, -1, -10, 6]
positive_list = []
negative_list = []
for num in nums:
    if num >= 0:
        positive_list.append(num)
    else:
        negative_list.append(num)
for i in range(len(positive_list)):
    nums[2*i] = positive_list[i]
    nums[(2*i) + 1] = negative_list[i]
print(nums)