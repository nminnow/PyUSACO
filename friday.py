'''
ID: audrey.6
LANG: PYTHON3
PROB: friday
'''

with open('friday.in') as fin:
    n = int(next(fin).rstrip())

d = 0
weekdays = {
    '6': 0,
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0
    }
months = {
    '1': 31,
    '2': 0,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
    } # use a list

for y in range(1900, 1900 + n):
    if y % 4 == 0 and y % 100 != 0 or y % 4 == 0 and y % 400 == 0: # combine % 100 and % 400
        months['2'] = 29
    else:
        months['2'] = 28

    for m in months:
        d += 13
        weekdays[str(d % 7)] += 1
        d += months[m] - 13

with open('friday.out', 'w') as fout:
    fout.write(' '.join(map(str, weekdays.values())))
    fout.write('\n')
