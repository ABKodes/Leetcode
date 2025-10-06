class MapSum:
    def __init__(self):
        self.dict = {}

    def insert(self, key, val):
        self.dict[key] = val

    def sum(self, prefix):
        ans = 0
        for k in self.dict:
            if k.startswith(prefix):
                ans += self.dict[k]
        return ans