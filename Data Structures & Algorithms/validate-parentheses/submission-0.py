class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        m = {')' : '(', ']':'[', '}':'{'}
        for c in s:
            if c in ['(','[','{']:
                q.append(c)
            else:
                if len(q) == 0 or m[c] != q[-1]:
                    return False
                q.pop()

        return len(q) == 0
        