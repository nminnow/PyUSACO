'''
ID: audrey.6
LANG: PYTHON3
PROB: combo
'''

with open('combo.in') as fin:
    n = int(next(fin).rstrip())
    fkey = list(map(int, next(fin).rstrip().split()))
    mkey = list(map(int, next(fin).rstrip().split()))

ans = 0
keys = []
for a in range(1, n + 1):
    if abs(fkey[0] - a) < 3 or n - 3 < abs(fkey[0] - a) < n + 3:
        for b in range(1, n + 1):
            if abs(fkey[1] - b) < 3 or n - 3 < abs(fkey[1] - b) < n + 3:
                for c in range(1, n + 1):
                    if abs(fkey[2] - c) < 3 or n - 3 < abs(fkey[2] - c) < n + 3:
                        keys.append((a, b, c))
                        ans += 1
for a in range(1, n + 1):
    if abs(mkey[0] - a) < 3 or n - 3 < abs(mkey[0] - a) < n + 3:
        for b in range(1, n + 1):
            if abs(mkey[1] - b) < 3 or n - 3 < abs(mkey[1] - b) < n + 3:
                for c in range(1, n + 1):
                    if abs(mkey[2] - c) < 3 or n - 3 < abs(mkey[2] - c) < n + 3:
                        if (a, b, c) not in keys:
                            ans += 1

with open('combo.out', 'w') as fout:
    fout.write(str(ans) + '\n')