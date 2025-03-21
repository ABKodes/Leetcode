class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        counter1 = Counter(s1)
        counter2 = Counter()
        left = 0
        for right in range(len2):
            counter2[s2[right]] += 1
            if right - left + 1 > len1:
                counter2[s2[left]] -=1
                if counter2[s2[left]] == 0:
                    del counter2[s2[left]]
                left += 1
            if counter1 == counter2:
                return True
        return False