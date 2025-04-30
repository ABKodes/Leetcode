class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        # Append the index of the parties
        for index, party in enumerate(senate):
            if party == "R":
                radiant.append(index)
            else:
                dire.append(index)
        # Compare the index
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"