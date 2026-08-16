# input of integer array nums with length n. output new array ans.
# ans array must be length of 2n.

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums

        for i in range(len(nums)):
            nums.append(nums[i])

        return ans
        