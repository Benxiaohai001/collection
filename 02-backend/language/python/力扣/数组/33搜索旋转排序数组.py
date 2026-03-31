class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        zh = (n - 1)  // 2
        left = 0
        right = n - 1
        print("test begin")
        print(f"nums: {nums}, target: {target}")
        while zh >= 0 and zh <= n-1:
            # print(11111)
            print(f"left: {left}, zh: {zh}, right: {right}")
            if nums[zh] == target:
                return zh
            if left == right:
                return -1
            if left == zh:
                if nums[right] == target:
                    return right
                else:
                    return -1
            if nums[zh] > nums[left]:
                if target < nums[zh] and target >= nums[left]:
                    right = zh
                    zh = (right + left) // 2
                else:
                    left = zh
                    zh = (left + right) // 2
            else:
                if target > nums[zh] and target <= nums[right]:
                    left = zh
                    zh  = (left + right) // 2
                else:
                    right = zh 
                    zh = (right + left) // 2


if __name__ == "__main__":
    s = Solution()
    # li = [4,5,6,7,0,1,2]
    # li = [1,3]
    # li = [1,3,5]
    li = [5,1,3] # 1
    print(s.search(li, 3))