# 13. 罗马数字转整数
class Solution:
    def romanToInt(self, s: str) -> int:
        li = []
        for i in s:
            if i == 'I':
                li.append(1)
            elif i == 'V':
                li.append(5)
            elif i == 'X':
                li.append(10)
            elif i == 'L':
                li.append(50)
            elif i == "C":
                li.append(100)
            elif i == 'D':
                li.append(500)
            else:
                li.append(1000)
        sum = 0
        for i in range(len(li)):
            if i >= 1 and li[len(li) - 1 - i] < li[len(li) - i]:
                sum -= li[len(li) - 1 - i]
            else:
                sum += li[len(li) - 1 - i]
            print(f"i = {i}, sum = {sum}, li[len(li) - 1 - i] = {li[len(li) - 1 - i]}, li[len(li) - 1 - i - 1] = {li[len(li) - 1 - i - 1]}")
        return sum 

if __name__ == "__main__":
    s = Solution()
    # print(s.romanToInt("LVIII"))
    print(s.romanToInt("MCMXCIV"))