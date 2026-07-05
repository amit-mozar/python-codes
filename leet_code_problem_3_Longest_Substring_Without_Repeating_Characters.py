# brute force way takes o(n2) time complexity
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        else:
            str_list = []
            for i in range(len(s)):
                new_str = s[i]
                for j in range(i+1, len(s)):
                    if s[j] not in new_str:
                        new_str += s[j]
                    else:
                        break
                str_list.append(len(new_str))
            return(max(str_list))
#        str_dict = {}
#        for i in str_list:
#            str_dict[i] = len(i)
#        print(str_list)
#        print(str_dict)
find_length = Solution()
string = 'pwwkew'
result = find_length.lengthOfLongestSubstring(string)
print(result)


# best way - optimal window
class solution_2:
    def lenghoflongeststring(self, s):
        chars = set()
        l = 0
        max = 0
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[i])
            length = i - l + 1
            if length > max:
                max = length
        print(chars)
        return max

optimal = solution_2()
result_2 = optimal.lenghoflongeststring(string)
print(result_2)
