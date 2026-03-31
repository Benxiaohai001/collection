class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        li = ["1", '11']
        for i in range(2, n):
            j = 0
            while j < len(li[i-1]):
                h = j + 1
                count = 1
                st = ''
                if h + 1 < len(li[i-1]):
                    while li[i-1][j] == li[i-1][h]:
                        if h + 1 < len(li[i-1]):
                            h += 1
                            count += 1
                        else:
                            st = st + str(count+1) + str(li[i-1][j])
                            break
                else:
                    st = st + str(count+1) + str(li[i-1][j])
                print(f"i: {i}, j: {j}, h: {h}, count: {count}, st: {st}")
                j += h
            li.append(st)
                # j = j + h
        print(li)
        return li[n - 1]

        
if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(4))