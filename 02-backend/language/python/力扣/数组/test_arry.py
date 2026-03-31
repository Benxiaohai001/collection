class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = []
        i = j = 0
        is_two = (len(nums1) + len(nums2))%2
        harf_len = (len(nums1) + len(nums2)) // 2
        while len(nums3) <= harf_len + 1:
            print(f"nums3: {nums3}, i: {i}, j: {j}")
            if i <= len(nums1) - 1  and j <= len(nums2) - 1:
                if nums1[i] <= nums2[j]:
                    nums3.append(nums1[i])
                    i = i+1
                else:
                    nums3.append(nums2[j])
                    j = j+1
            elif i <= len(nums1) - 1:
                print(22222222222)
                nums3 = nums3 + nums1[i:]
            else:
                print(1111111111)
                nums3 = nums3 + nums2[j:]
        if is_two == 1:
            print(f"nums3: {nums3}")
            return nums3[harf_len]
        else:
            print(f"nums3: {nums3}")
            return (nums3[harf_len] + nums3[harf_len+1])/2

if __name__ == '__main__':
    s = Solution()
    # print(s.findMedianSortedArrays([1,2],[3, 4]))
    print(s.findMedianSortedArrays([1,3],[2]))
    # print(s.findMedianSortedArrays([1,2],[3,4]))
    # print(s.findMedianSortedArrays([0,0],[0,0]))
    # print(s.findMedianSortedArrays([],[1]))
    # print(s.findMedianSortedArrays([2],[]))