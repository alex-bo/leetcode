

class Solution:

    def pushDominoes(self, dominoes: str) -> str:
        if not dominoes:
            return dominoes

        res = list(dominoes)
        le, ri = None, None
        for i in range(len(res)):
            if res[i] == '.':
                continue
            if le is None:
                le = i
                continue
            ri = i
            while (res[le] == 'R' and res[ri] == 'L' and (ri - le) > 2) \
                    or (res[le] == 'R' and res[ri] == 'R' or res[le] == 'L' and res[ri] == 'L') and le < ri:
                if res[le] == 'R':
                    le += 1
                    res[le] = 'R'
                if res[ri] == 'L':
                    ri -= 1
                    res[ri] = 'L'
            le = i

        # deal with left edge
        for i in range(len(res)):
            if res[i] == 'R':
                break
            if res[i] == 'L':
                for j in range(i):
                    res[j] = 'L'

        # deal with right edge
        for i in range(len(res) - 1, -1, -1):
            if res[i] == 'L':
                break
            if res[i] == 'R':
                for j in range(i + 1, len(res)):
                    res[j] = 'R'

        return ''.join(res)


if __name__ == '__main__':
    print('RR.L', Solution().pushDominoes('RR.L'))
    print('LL.RR.LLRRLL..', Solution().pushDominoes('.L.R...LR..L..'))
    print('RRR.L', Solution().pushDominoes('R.R.L'))
