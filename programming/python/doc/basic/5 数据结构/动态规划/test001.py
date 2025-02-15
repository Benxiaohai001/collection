# 198. 打家劫舍
class Solution:
    def rob(self, nums: list[int]) -> int:
        # n = len(nums)
        # li = [nums[0]] + [0] * n
        # if n == 1:
        #     return nums[0]
        # for i in range(1, n):
        #     if i == 1:
        #         if nums[0] < nums[1]:
        #             li[1] = nums[1]
        #         else:
        #             li[1] = nums[0]
        #         continue
            
        #     if li[i-2] + nums[i] > li[i-1]:
        #         li[i] = li[i-2] + nums[i]
        #     else:
        #         li[i] = li[i-1]  
        #     print(f"li: {li}")
        # return max(li)
        n = len(nums)
        if n == 1:
            return nums[0]
        li = [nums[0], max(nums[0], nums[1])] + [0] * n
        for i in range(2, n):
            li[i] = max(li[i-2] + nums[i], li[i-1])
        return max(li)


if __name__ == "__main__":
    s = Solution()
    nums = [2,1,1,2]
    print(s.rob(nums))