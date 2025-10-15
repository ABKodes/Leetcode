class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def occ(text: str, pat: str) -> List[int]:
            if not pat:
                return []
            pi = [0] * len(pat)
            j = 0
            for i in range(1, len(pat)):
                while j and pat[j] != pat[i]:
                    j = pi[j - 1]
                if pat[j] == pat[i]:
                    j += 1
                pi[i] = j
            res = []
            j = 0
            for i, ch in enumerate(text):
                while j and pat[j] != ch:
                    j = pi[j - 1]
                if pat[j] == ch:
                    j += 1
                    if j == len(pat):
                        res.append(i - len(pat) + 1)
                        j = pi[j - 1]
            return res

        A = occ(s, a)
        B = occ(s, b)
        res = []
        j = 0
        for i in A:
            while j < len(B) and B[j] < i - k:
                j += 1
            if j < len(B) and B[j] <= i + k:
                res.append(i)
        return res
