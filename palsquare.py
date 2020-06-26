'''
ID: audrey.6
LANG: PYTHON3
PROB: palsquare
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

def to_b(x, b):
    m = 16
    while x // b ** m < 1:
        m -= 1
    bx = ''
    r = x
    for p in range(m, -1, -1):
        q = r // b ** p
        bx += str(q) if q < 10 else DIG[q]
        r -= q * b ** p
    return bx

with open('palsquare.in') as fin:
    b = int(next(fin).rstrip())

bns = []
for n in range(1, 301):
    s = n ** 2
    bs = to_b(s, b)
    f = bs[:(len(bs) - 1) // 2] if len(bs) % 2 else bs[:len(bs) // 2]
    if bs[:len(f)] == bs[::-1][:len(f)]:
        bn = to_b(n, b)
        bns.append((bn, bs))

with open('palsquare.out', 'w') as fout:
    if bns:
        for bn, bs in bns:
            fout.write(bn + ' ' + bs + '\n')
    else:
        fout.write('\n')
