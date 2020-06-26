'''
ID: audrey.6
LANG: PYTHON3
PROB: transform
'''

def transform():
    cpy = org
    for p in range(3):
        rot = []
        for q in range(n):
            temp = []
            for r in range(n):
                temp.append(cpy[r][q])
            temp.reverse()
            rot.append(temp)
        if rot == tar:
            return p + 1
        cpy = rot

    rev = []
    for r in org:
        r.reverse()
        rev.append(r)
    if rev == tar:
        return 4

    rpy = rev
    for p in range(3):
        rvt = []
        for q in range(n):
            temp = []
            for r in range(n):
                temp.append(rpy[r][q])
            temp.reverse()
            rvt.append(temp)
        if rvt == tar:
            return 5
        rpy = rvt

    if org == tar:
        return 6

    return 7

with open('transform.in') as fin:
    n = int(next(fin).rstrip())
    org = []
    for r in range(n):
        org.append(list(next(fin).rstrip()))
    tar = []
    for r in range(n):
        tar.append(list(next(fin).rstrip()))

with open('transform.out', 'w') as fout:
    fout.write(str(transform()) + '\n')
