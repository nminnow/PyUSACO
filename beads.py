'''
ID: audrey.6
LANG: PYTHON3
PROB: beads
'''

def count():
    lens = []
    pb = 0
    pbead = ''
    for b, bead in enumerate(beads * 2):
        if bead != 'w':
            if not pbead:
                pbead = bead
            if bead != pbead:
                pbead = bead
                lens.append(b - pb)
                pb = b
    if not lens:
        lens.append(l)

    maxlen = 0
    plen = 0
    for len in lens:
        length = len + plen
        if maxlen < length <= l:
            maxlen = length
        plen = len
    return maxlen

with open('beads.in') as fin:
    l = int(next(fin).rstrip())
    beads = list(next(fin).rstrip())

with open('beads.out', 'w') as fout:
    maxlen1 = count()
    beads.reverse()
    maxlen2 = count()
    print(maxlen1, maxlen2)
    fout.write(str(max([maxlen1, maxlen2])) + '\n')
