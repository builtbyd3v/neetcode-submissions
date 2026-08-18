class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        sorted_pairs = list(sorted(count.items(), key=lambda item: item[1], reverse=True))
        new_list = []

        for pair in sorted_pairs:
            new_list.append(pair[0])

        return new_list[:k]
