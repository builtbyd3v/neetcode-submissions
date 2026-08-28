class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            srtd = "".join(sorted(word))

            if srtd in seen:
                seen[srtd].append(word)
            else:
                seen[srtd] = [word]

        return list(seen.values())