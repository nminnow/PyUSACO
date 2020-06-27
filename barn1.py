'''
ID: audrey.6
LANG: PYTHON3
PROB: barn1
'''

with open('barn1.in') as fin:
    M, S, C = map(int, next(fin).rstrip().split())
    stalls = [0 for _ in range(S)]
    for _ in range(C):
        stalls[int(next(fin).rstrip()) - 1] = 1

boards = stalls.copy()

m = 0
cont = False
for board in boards:
    if board:
        if not cont:
            cont = True
            m += 1
    else:
        if cont:
            cont = False

blocked = C
while m > M:
    span = (0, 0)
    mgap = S
    gap = 0
    pb = -1
    for b, board in enumerate(boards):
        if board:
            if mgap > gap > 0 and pb > -1:
                mgap = gap
                span = (pb, b)
            gap = 0
            pb = b
        else:
            gap += 1
    for b in range(span[0], span[1]):
        boards[b] = 1

    blocked = 0
    for board in boards:
        if board:
            blocked += 1

    m = 0
    cont = False
    for board in boards:
        if board:
            if not cont:
                cont = True
                m += 1
        else:
            if cont:
                cont = False

with open('barn1.out', 'w') as fout:
    fout.write(str(blocked) + '\n')
