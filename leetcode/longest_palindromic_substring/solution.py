class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0

        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i + 1)
            
            lenm = max(len1, len2)

            if(lenm > end - start):
                start = i - (lenm - 1) // 2
                end = i + lenm // 2

        return s[start:end + 1]

    def expand_around_center(self, s: str, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
        

result = Solution().longestPalindrome("babads")
print(result)

result = Solution().longestPalindrome("cbbd")
print(result)

result = Solution().longestPalindrome("tattarrattat")
print(result)