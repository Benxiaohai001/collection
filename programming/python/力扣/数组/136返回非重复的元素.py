class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        for i in range(1, n-1):
            print(f"i: {i}, nums[i]: {nums[i]}, nums[i-1]: {nums[i-1]}, nums[i+1]: {nums[i+1]}")
            if nums[i] == nums[i-1] or nums[i] == nums[i+1]:
                continue
            else:
                return nums[i]
        if nums[0] == nums[1]:
            print(f"nums[-1]: {nums[-1]}")
            return nums[-1]
        else:
            print(f"nums[0]: {nums[0]}")
            return nums[0]

if __name__ == "__main__":
    s = Solution()
    li = [4,1,2,1,2]
    print(s.singleNumber(li))
