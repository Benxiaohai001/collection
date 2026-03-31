class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while (i >= 0 and i < n-1) and nums[i] >= nums[i+1]:
            i -= 1
            print(f"i {i}, nums[i] {nums[i]}, nums[i+1] {nums[i+1]}, nums {nums}")
            if i < 0:
                nums.reverse()
                break
        j = n - 1
        while j > i and nums[j]<=nums[i]:
            j -= 1
        
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        tmp_list = nums[i+1:]
        tmp_list.reverse()
        for k in range(i+1, n):
            nums[k] = tmp_list[k-i-1]
        print(nums)
        
if __name__ == "__main__":
    s = Solution()
    # li = [1,2,3] # [1,3,2]
    # li = [3, 2, 1]
    li = [1,3,2] # [2,1,3]
    s.nextPermutation(li)
    # print(li) # [1,3,2]