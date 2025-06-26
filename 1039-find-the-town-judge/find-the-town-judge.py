class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_received = [0] * (n + 1)
        trust_given = [0] * (n + 1)

        for giver, receiver in trust:
            trust_given[giver] += 1
            trust_received[receiver] += 1

        for person in range(1, n + 1):
            if trust_given[person] == 0 and trust_received[person] == n - 1:
                return person  
                
        return -1

        