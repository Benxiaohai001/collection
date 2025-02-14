# [27 移除元素](https://leetcode-cn.com/problems/remove-element/)
# 快慢指针
# 优化
# 左右指针

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
        left = 0
        n = len(nums)
        if n == 1:
            if nums[left] != val:
                return left + 1
            else:
                return 0
        print(f"n: {n}, nums: {nums}, target: {val}")
        right = n - 1
        while left < right:
            print(f"left: {left}, right: {right}, nums: {nums}, target: {val}")
            if nums[left] != val:
                left += 1
                continue
            if nums[right] != val:
                nums[left] = nums[right]
            right -= 1
        if nums[left] == val:
            left -= 1
            print(f"left: {left}")
        

        return left + 1


# 快慢指针
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                # print(f"nums: {nums}")
            else:
                left += 1
        return left
'''


if __name__ == "__main__":
    s = Solution()
    # li = [3,2,2,3]
    li = [3, 3]
    print(s.removeElement(li, 3))