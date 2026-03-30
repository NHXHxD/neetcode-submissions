class Solution:
    def checkValidString(self, s: str) -> bool:
        free = []
        op = []
        for i, c in enumerate(s):
            if c == "(":
                op.append(i)
            elif c == "*":
                free.append(i)
            else:
                if op:
                    op.pop()
                else:
                    if free:
                        idx = free.pop()
                    else:
                        return False
        while op and free:
            op_i = op.pop()
            s_i = free.pop()
            if op_i > s_i:
                return False

        return True if not op else False