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




if __name__ == "__main__":
    s = Solution()
    # li = [3,2,2,3]
    li = [3, 3]
    print(s.removeElement(li, 3))