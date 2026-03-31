import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        print(f"lower_s: {lower_s}")
        remove_s = re.sub(r"[^a-zA-Z0-9]", '', lower_s)
        n = len(remove_s)
        print(f"remove_s: {remove_s}")
        if n <= 1:
            return True
        i, j = 0, n-1
        while i < j:
            print(f"i:{i}, j: {j}, remove_s[i]: {remove_s[i]}, remove_s[j]: {remove_s[j]}")
            if remove_s[i] != remove_s[j]:
                return False
            i += 1
            j -= 1
        return True
if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    print(solution.isPalindrome(s))