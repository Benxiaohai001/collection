class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums = list(set(nums))
        lenth = len(nums)
        return lenth
        

if __name__ == "__main__":
    s = Solution()
    li = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(li))
    print(li)