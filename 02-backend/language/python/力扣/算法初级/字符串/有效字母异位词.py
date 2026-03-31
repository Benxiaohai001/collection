class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = dict()
        hash_t = dict()
        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]] = 1
        for j in range(len(t)):
            if t[j] in hash_t:
                hash_t[t[j]] += 1
            else:
                hash_t[t[j]] = 1
        for si in hash_s:
            if si not in hash_t:
                return False
            if hash_s[si] != hash_t[si]:
                return False
        return True

if __name__ == '__main__':
    s = "tac"
    t = "rac"
    solution = Solution()
    # print("--------------------")
    print(solution.isAnagram(s, t))