class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        srtd_s = "".join(sorted(s))
        srtd_t = "".join(sorted(t))

        if srtd_s == srtd_t:
            return True
            
        return False