class Trie:
    def __init__(self):
        self.nodes = []
        self.cnts = []
        self.new_node()

    def new_node(self):
        self.nodes.append([-1] * 26)
        self.cnts.append(0)
        return len(self.nodes) - 1

    def add(self, s, d):
        for i in range(len(s)):
            curr = 0
            for j in range(i, len(s)):
                x = ord(s[j]) - ord('a')
                if self.nodes[curr][x] == -1:
                    self.nodes[curr][x] = self.new_node()
                curr = self.nodes[curr][x]
                self.cnts[curr] += d

    def query(self, s):
        result = (float("inf"), "")
        for i in range(len(s)):
            curr = 0
            for j in range(i, len(s)):
                x = ord(s[j]) - ord('a')
                if self.nodes[curr][x] == -1:
                    break
                curr = self.nodes[curr][x]
                if self.cnts[curr] == 0:
                    result = min(result, (j - i + 1, s[i:j + 1]))
                    break
        return result[1]


class Solution:
    def shortestSubstrings(self, arr):
        trie = Trie()
        for x in arr:
            trie.add(x, +1)
        result = []
        for x in arr:
            trie.add(x, -1)
            result.append(trie.query(x))
            trie.add(x, +1)
        return result
