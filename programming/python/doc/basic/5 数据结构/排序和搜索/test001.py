class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point1, point2 = 0, 0
        while point1 < m or point2 < n:
            print(f"point1: {point1}, point2: {point2}, m: {m}, n: {n}")
            # if point1 
            if point1 >= m:
                nums1[point1:] = nums2[point2:]
                return
            if point2 >= n:
                return
            if nums2[point2] < nums1[point1]:
                nums1.insert(point1, nums2[point2])
                nums1.pop()
                point2 += 1
                point1 += 1
                m += 1
            else:
                point1 += 1

if __name__ == '__main__':
    s = Solution()
    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    for i in nums1:
        print(i, end=' ')
# print()
            