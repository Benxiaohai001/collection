class Solution:
    def climbStairs(self, n: int) -> int:
        li = [0] * n
        li[0] = 1
        li[1] = 2
        if n > 2:
            for i in range(2, n):
                li[i] = li[i-1] + li[i-2]
        return li[n-1]
if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))