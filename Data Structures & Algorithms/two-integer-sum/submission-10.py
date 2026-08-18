#input: array of integers (nums), integer (target). output: return indices i and j when i + j = target and i is not equal to j.
#nested for loop for i and j on length of nums. check if each i equals to target when each j is added. return the first pair that equals to target

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = 1
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]