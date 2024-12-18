class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 暴力解析
        # for j in range(n):
        #     nums1.pop() 
        # for i in nums2:
        #     if not nums1:
        #         nums1.append(i)
        #         m += 1
        #         continue
        #     for index, value in enumerate(nums1):
        #         print(f"i: {i}, index: {index}, value: {value}, nums1: {nums1}, m: {m}")
        #         if i <= value:
        #             nums1.insert(index, i)
        #             m += 1
        #             break
        #         if index == m-1:
        #             nums1.insert(index+1, i)
        #             m += 1
        #             break


        # 拼接后排序
        # print(f"nums1: {nums1}, m: {m}, nums2: {nums2}, n: {n}")
        # nums1[m:] = nums2
        # print(f"nums1: {nums1}")
        # nums1.sort()


        # 双指针
        p1 = 0
        p2 = 0
        for p2 in range(len(nums2)):
            if m == 0:
                print(f"nums1: {nums1}, m: {m}, nums2: {nums2}, n: {n}")
                nums1[:] = nums2
                break
            if nums2[p2] > nums1[m-1]:
                nums1.insert(m, nums2[p2])
                nums1.pop()
                m += 1
                continue
            while p1 < m:
                if nums2[p2] <= nums1[p1]:
                    nums1.insert(p1, nums2[p2])
                    nums1.pop()
                    p1 += 1 
                    m += 1
                    break
                p1 += 1


if __name__ == "__main__":
    s = Solution()
    # li = [1,2,3,0,0,0]
    # li2 = [2,5,6]
    li = [0]
    li2 = [1]
    s.merge(li, 0, li2, 1)
    print(li)