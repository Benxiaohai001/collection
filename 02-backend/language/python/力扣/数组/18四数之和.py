class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        length = len(nums)
        result = []
        for first in range(length-3):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            for second in range(first+1, length - 2):
                if second > first+1  and nums[second] == nums[second - 1]:
                    continue
                forth = length - 1 
                third = second + 1
                while third < forth:
                    fore_sum = nums[first] + nums[second] + nums[third] + nums[forth]
                    if fore_sum == target:
                        print(f"first: {first}, second: {second}, third: {third}, forth: {forth}");
                        result.append([nums[first], nums[second], nums[third], nums[forth]])
                        third += 1
                        while third < forth and nums[third] == nums[third -1]:
                            print(f"first: {first}, second: {second}, third: {third}, forth: {forth}");
                            third += 1
                    elif fore_sum > target:
                        forth -= 1
                        while third < forth and nums[forth] == nums[forth + 1]:
                            print(f"first: {first}, second: {second}, third: {third}, forth: {forth}");
                            forth -= 1
                    else:
                        third += 1
                        while third < forth and nums[third] == nums[third -1]:
                            print(f"first: {first}, second: {second}, third: {third}, forth: {forth}");
                            third += 1
        return result

if __name__ == "__main__":
    s = Solution()
    # li = [2,2,2,2,2]
    li = [-2,-1,-1,1,1,2,2]
    print(s.fourSum(li, 0))