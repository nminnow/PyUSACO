'''
ID: audrey.6
LANG: PYTHON3
PROB: dualpal
'''

DIG = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
    16: 'G',
    17: 'H',
    18: 'I',
    19: 'J'
    }

def check_dup(x):
    pal = 0
    for b in range(2, 11):
        m = 0
        while x // b ** (m + 1) > 0:
            m += 1
        bx = ''
        r = x
        for p in range(m, -1, -1):
            q = r // b ** p
            bx += str(q) if q < 10 else DIG[q]
            r -= q * b ** p
        f = bx[:(len(bx) - 1) // 2] if len(bx) % 2 else bx[:len(bx) // 2]
        if bx[:len(f)] == bx[::-1][:len(f)]:
            pal += 1
            if pal == 2:
                return True

with open('dualpal.in') as fin:
    n, s = map(int, next(fin).rstrip().split())

dups = []
x = s + 1
while len(dups) < n:
    if check_dup(x):
        dups.append(str(x))
    x += 1

with open('dualpal.out', 'w') as fout:
    fout.write('\n'.join(dups) + '\n')
