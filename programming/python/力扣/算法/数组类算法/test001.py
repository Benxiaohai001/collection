# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # nums.sort()
#         count = 0
#         for i in range(len(nums)):
#             # j = 0
#             print(f"i: {i}, count: {count}")
#             while nums[i - count] == 0:
#                 # print(f"i: {i}, count: {count}, nums: {nums}")
#                 nums.append(nums.pop(i-count))
#                 print(f"nums: {nums}")
#                 count += 1
#                 break

# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             while left < right and nums[right] == val:
#                 print(f"right: {right}, left: {left}")
#                 right -= 1
#                 print(f"nums: {nums}")
#             print('111111111')
#             if nums[left] == val:
#                 nums[left], nums[right] = nums[right], nums[left]
#                 right -= 1
#                 print(f"nums: {nums}")
#             left += 1
#         return left


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        slow = fast = 2
        while fast < n:
            print(f"slow: {slow}, fast: {fast}, nums: {nums}")
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
            print(f"slow: {slow}, fast: {fast}, nums: {nums}")
        return slow

if __name__ == '__main__':
    s = Solution()
    # nums = [0,1,2,2,3,0,4,2]
    # nums = [1, 2, 3]
    nums = [1,1,1,2,2,3]
    print(s.removeDuplicates(nums))
    # print(nums)