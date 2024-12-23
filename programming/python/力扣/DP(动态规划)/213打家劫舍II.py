class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        if n == 3:
            return max(nums[0], nums[1], nums[2])
        li = [nums[0], max(nums[0], nums[1])] + [0] * n
        for i in range(2, n - 1):
            li[i] = max(li[i - 2] + nums[i], li[i - 1])
        li1 = [0, nums[1], max(nums[1], nums[2])] + [0] * n
        for j in range(3, n):
            print(f"j: {j},li1: {li1}, li[j-1]: {li1[j-1]}, li1[j-2]: {li1[j-2]}, nums[j]: {nums[j]}")
            li1[j] = max(li1[j - 2] + nums[j], li1[j - 1])
        print(f"li: {li}, li1: {li1}")
        return max(max(li), max(li1))

if __name__ == "__main__":
    s = Solution()
    # li = [1,7,9,2]
    # nums = [6,6,4,8,4,3,3,10]
    nums = [6,3,10,8,2,10,3,5,10,5,3]
    print(s.rob(nums))