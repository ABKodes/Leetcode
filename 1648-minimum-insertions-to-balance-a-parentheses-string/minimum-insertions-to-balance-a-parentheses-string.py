class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        need = 0
        for char in s:
            if char == "(":
                need += 2
                if need % 2 == 1:
                    insertions += 1
                    need -= 1
            else:
                need -= 1
                if need < 0:
                    insertions += 1
                    need = 1
        insertions += need 
        return insertions