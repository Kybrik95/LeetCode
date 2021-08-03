class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        duo = [-1, -1]
        dct = {}
        for i, num in enumerate(nums):
            j = dct.get(target - num)
            if j is not None:
                duo = [j, i]
                break
            dct[num] = i
        return duo
