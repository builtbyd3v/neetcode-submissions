class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = defaultdict(list)

        for s in strs:
            sort["".join(sorted(s))].append(s)
        return list(sort.values())