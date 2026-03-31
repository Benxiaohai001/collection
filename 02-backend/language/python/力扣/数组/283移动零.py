class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        fast = slow = 0
        while fast < n:
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
            print(f"nums: {nums} slow: {slow} fast: {fast}")
if __name__ == "__main__":
    s = Solution()
    li = [0,1,0,3,12]
    s.moveZeroes(li)
    print(li)