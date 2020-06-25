'''
ID: audrey.6
LANG: PYTHON3
PROB: beads
'''

with open('beads.in') as fin:
    t = int(next(fin).rstrip())
    beads = list(next(fin).rstrip())

maxlen = 0
for b, bead in enumerate(beads):
    switch = 2
    len = 0
    x = b + 1
    if bead == 'w':
        while x % t != b % t:
            xbead = beads[x % t]
            if xbead != 'w':
                pbead = xbead
                while switch and x % t != b % t:
                    xbead = beads[x % t]
                    if xbead != 'w' and xbead != pbead:
                        switch -= 1
                        pbead = xbead
                    len += 1
                    x += 1
                break
            len += 1
            x += 1
        else:
            len = t
    else:
        pbead = bead
        while switch and x % t != b % t:
            xbead = beads[x % t]
            if xbead != 'w' and xbead != pbead:
                switch -= 1
                pbead = xbead
            len += 1
            x += 1
        if switch:
            len += 1
    if maxlen < len:
        maxlen = len

with open('beads.out', 'w') as fout:
    fout.write(str(maxlen) + '\n')
