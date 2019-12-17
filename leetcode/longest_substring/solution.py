class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = start = 0
        dic = {}

        for i, item in enumerate(s):
            if item in dic: 
                start = max(dic[item], start)
            else:
                dic[item] = start

            res = max(res, i - start + 1)
            dic[item] = i + 1

        return res

result = Solution().lengthOfLongestSubstring("abcabcbb")
print(result)

result = Solution().lengthOfLongestSubstring("bbbbb")
print(result)

result = Solution().lengthOfLongestSubstring("pwwkew")
print(result)

result = Solution().lengthOfLongestSubstring("aab")
print(result)

result = Solution().lengthOfLongestSubstring("dvdf")
print(result)

result = Solution().lengthOfLongestSubstring("dvdfafbcrtgszm")
print(result)