# input: array of strings (strs). output: list with sublists of grouped anagrams.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord in seen:
                seen[sortedWord].append(word)
            else:
                seen[sortedWord] = [word]
        
        return list(seen.values())