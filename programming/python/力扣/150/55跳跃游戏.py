class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        n = len(nums)
        dp = [nums[0]] * n
        print(f"dp: {dp}, nums: {nums}")
        for i in range(1, n):
            print(f"i: {i}, dp: {dp}")
            print(f"")
            dp[i] = max(dp[i-1], dp[i - 1] + i)
            print(f"i: {i}, dp: {dp}")
            if dp[i] > n - 1:
                return True
        return False
if __name__ == "__main__":
    s = Solution()
    # li = [2,3,1,1,4]
    li = [3,2,1,0,4]
    print(s.canJump(li))