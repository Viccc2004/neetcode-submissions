class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = Counter(s)
        t_set = Counter(t)
        print(s_set)
        print(t_set)
        return s_set == t_set