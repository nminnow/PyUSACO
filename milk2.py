'''
ID: audrey.6
LANG: PYTHON3
PROB: milk2
'''

with open('milk2.in') as fin:
    n = int(next(fin).rstrip())
    times = []
    for _ in range(n):
        times.append(list(map(int, next(fin).rstrip().split())))
    if not times:
        times.append([0, 0])

if times:
    conts = [0]
    idles = [0]
    cont = False
    idle = False
    duration = 0
    for t in range(min(time[0] for time in times), max(time[1] for time in times)):
        m = 0
        for start, end in times:
            if t in range(start, end):
                m = 1
                break
        if cont:
            if m:
                duration += 1
            else:
                conts.append(duration)
                cont = False
                idle = True
                duration = 1
        elif idle:
            if m:
                idles.append(duration)
                idle = False
                cont = True
                duration = 1
            else:
                duration += 1
        else:
            if m:
                cont = True
                duration = 1
            else:
                idle = True
                duration = 1
    if cont:
        conts.append(duration)
    elif idle:
        idles.append(duration)

with open('milk2.out', 'w') as fout:
    fout.write(str(max(conts)) + ' ' + str(max(idles)) + '\n')
