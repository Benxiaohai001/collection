class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 0
        for fast in range(n):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            # if 
        return slow

if __name__ == "__main__":
    s = Solution()
    li = [3,2,2,3]
    print(s.removeElement(li, 3))
    print(li)
