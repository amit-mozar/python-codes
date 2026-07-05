class Solution(object):
    def twoSum(self, nums, target):
        mp={}
        for i in range(len(nums)):
            diff=target-nums[i]    #jo number chahiye
            if diff in mp:
                print(mp)
                print([mp[diff],i])
                return [mp[diff],i]  #check karo pahle aya h ki nhi
            mp[nums[i]]=i
            print(mp)

nums = [2,7,11,15]
target = 17
two_sums = Solution()
sol = two_sums.twoSum(nums, target)
print(sol)