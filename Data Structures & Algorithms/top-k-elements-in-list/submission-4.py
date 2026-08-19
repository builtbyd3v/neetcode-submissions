#input: array of ints (nums), and integer (k), return the k most frequent elements ([:k])

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1

        sorted_pairs = list(sorted(count.items(), key=lambda item: item[1], reverse=True))

        zero = []

        for pair in sorted_pairs:
            zero.append(pair[0])

        return zero[:k]
        