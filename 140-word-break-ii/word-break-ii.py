class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def searchWordEnd(self, prefix):
        curr = self.root
        ends = []
        for idx, char in enumerate(prefix):
            if char not in curr.children:
                break

            curr = curr.children[char]
            if curr.is_end:
                ends.append(idx + 1)
        return ends    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        memo = {}

        def bt(val):
            if val in memo:
                return memo[val]
            if not val:
                return [""]
            
            result = []
            for i in trie.searchWordEnd(val):
                word = val[:i]
                remain_sent = bt(val[i:])
                for res in remain_sent:
                    if res:
                        result.append(word +" " + res)
                    else:
                        result.append(word)
            memo[val] = result

            return result
        return bt(s)