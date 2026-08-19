# input: array of ints (nums) and an int (target).
# output: return i and j when i and j = target and do not equal each other (index).
# nested for loop i and j. i on range of length of nums and j on range of length of nums starting from i + 1.
# return first pair that equals to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        