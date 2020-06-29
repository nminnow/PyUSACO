'''
ID: audrey.6
LANG: PYTHON3
PROB: wormhole
'''

class Hole:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pair = None

    def walk(self):
        for hole in holes:
            if hole.y == self.y and hole.x > self.x:
                return hole

    def jump(self):
        return self.pair

def get_pairings(group):
    lgroup = list(group)
    
    if len(lgroup) == 2:
        return [[(lgroup[0], lgroup[1])]]

    pairings = []
    for r in range(1, len(group)):
        rpairings = get_pairings(group - {lgroup[0], lgroup[r]})
        pairings += [[(lgroup[0], lgroup[r])] + t for t in rpairings]
    return pairings

with open('wormhole.in') as fin:
    n = int(next(fin).rstrip())
    holes = []
    for _ in range(n):
        x, y = map(int, next(fin).rstrip().split())
        holes.append(Hole(x, y))

ans = 0
holes.sort(key=lambda hole: hole.x)
pairings = get_pairings(set(holes))
for pairing in pairings:
    for a, b in pairing:
        a.pair = b
        b.pair = a

    hascyc = False
    for hole in holes:
        nhole = hole.walk()
        wholes = []
        while nhole not in wholes:
            if not nhole:
                break
            wholes.append(nhole)
            nhole = nhole.jump().walk()
        else:
            hascyc = True
            break
    if hascyc:
        ans += 1

with open('wormhole.out', 'w') as fout:
    fout.write(f'{ans}\n')
