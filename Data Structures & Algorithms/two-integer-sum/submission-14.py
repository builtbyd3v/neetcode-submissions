#input: array of integers (nums), integer (target). output: return index of i and j when they equal target and do not equal each other

#implement: nested for loops, one starting at 0 (i) and one starting at 1(j).check if i + j == target and != each other, return first result where this is true.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        