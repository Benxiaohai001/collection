class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 1
        n = len(nums)
        if n == 1:
            return 1 
        fast = 1
        count = 1
        print(f"n: {n}, nums: {nums}")
        while fast < n:
            print(f"slow: {slow}, fast: {fast}, nums: {nums}")
            if nums[fast] != nums[fast - 1]:
                count = 1
                nums[slow] = nums[fast]
                slow += 1
            else:
                count += 1
                if count < 3:
                    nums[slow] = nums[fast]
                    slow += 1
                
            fast += 1
            print(f"slow: {slow}, fast: {fast}, nums: {nums}, count: {count}")
        for _ in range(n-slow):
            nums.pop()
        return slow

if __name__ == "__main__":
    s = Solution()
    li = [1,1,1,2,2,3]
    # li = [1,1,1,1]
    print(s.removeDuplicates(li))
    print(li)


        