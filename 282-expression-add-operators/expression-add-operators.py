class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(expr: str, pos: int, prev_val: int, curr_val: int):
            if pos == len(num):
                if curr_val == target:
                    res.append(expr)
                return

            for i in range(pos, len(num)):
                if i != pos and num[pos] == '0': # No leading zeros ofcourse!
                    break
                s = num[pos:i+1]
                v = int(s)

                if pos == 0:
                    backtrack(s, i + 1, v, v)
                else:
                    backtrack(expr + '+' + s, i + 1, v, curr_val + v)
                    backtrack(expr + '-' + s, i + 1, -v, curr_val - v)
                    backtrack(expr + '*' + s, i + 1,
                              prev_val * v,
                              curr_val - prev_val + prev_val * v)

        backtrack("", 0, 0, 0)
        return res
