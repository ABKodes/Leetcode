from collections import defaultdict, deque
class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        b = defaultdict(deque)
        for word in words:
            b[word[0]].append((word, 0))

        matches = 0
        for ch in s:
            current = b[ch]
            for _ in range(len(current)):
                word, pos = current.popleft()
                pos += 1
                if pos == len(word):
                    matches += 1
                else:
                    b[word[pos]].append((word, pos))
        return matches