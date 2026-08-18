#input: array of strings (strs). output: array in any order of all anagrams grouped into sublists

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        srtd = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord in srtd:
                srtd[sortedWord].append(word)
            else:
                srtd[sortedWord] = [word]
        
        return list(srtd.values())