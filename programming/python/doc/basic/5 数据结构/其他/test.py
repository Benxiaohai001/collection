class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        ans.append([1, 1])
        if numRows == 2:
            return ans
        print(f"ans = {ans}")
        for i in range(3, numRows + 1):
            li = [1]
            for j in range(1, i-1):
                print(f"i = {i}, j = {j}, ans[i-2][j-1] = {ans[i-2][j-1]}, ans[i-2][j] = {ans[i-2][j]}, li = {li}")
                li.append(ans[i-2][j-1] + ans[i-2][j])
            li.append(1)
            ans.append(li)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))