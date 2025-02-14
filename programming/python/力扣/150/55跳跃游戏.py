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

# 贪心算法
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

作者：力扣官方题解
链接：https://leetcode.cn/problems/jump-game/solutions/203549/tiao-yue-you-xi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
''' 
# 动态规划
#
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[0 for _ in range(len(nums))]
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            if dp[i-1]>=i: dp[i]=max(dp[i-1], i+nums[i])
            else: dp[i]=dp[i-1]
        return dp[-1]>=len(nums)-1
# 优化
def canJump(nums):
    max_len=nums[0]
    for i in range(1,len(nums)):
        if max_len>=i: max_len=max(max_len, i+nums[i])
    return max_len>=len(nums)-1

# 作者：yuer
# 链接：https://leetcode.cn/problems/jump-game/solutions/733857/tiao-yue-you-xi-dong-tai-gui-hua-jian-da-ndz1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
if __name__ == "__main__":
    s = Solution()
    # li = [2,3,1,1,4]
    li = [3,2,1,0,4]
    print(s.canJump(li))