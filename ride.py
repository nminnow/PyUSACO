"""
ID: audrey.6
LANG: PYTHON3
PROG: ride
"""

with open('ride.in') as f:
    cs = [ord(x) - 64 for x in next(f).rstrip()]
    gs = [ord(x) - 64 for x in next(f).rstrip()]

comet = 1
for c in cs:
    comet *= c

group = 1
for g in gs:
    group *= g

with open('ride.out', 'w') as f:
    if comet % 47 == group % 47:
        f.write('GO' + '\n')
    else:
        f.write('STAY' + '\n')
