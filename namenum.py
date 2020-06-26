'''
ID: audrey.6
LANG: PYTHON3
PROB: namenum
'''

KEY = {
    'A': '2',
    'B': '2',
    'C': '2',
    'D': '3',
    'E': '3',
    'F': '3',
    'G': '4',
    'H': '4',
    'I': '4',
    'J': '5',
    'K': '5',
    'L': '5',
    'M': '6',
    'N': '6',
    'O': '6',
    'P': '7',
    'Q': 'x',
    'R': '7',
    'S': '7',
    'T': '8',
    'U': '8',
    'V': '8',
    'W': '9',
    'X': '9',
    'Y': '9',
    'Z': 'x'
    }

with open('namenum.in') as fin:
    serial = next(fin).rstrip()

with open('dict.txt') as fict:
    names = []
    for line in fict:
        name = line.rstrip()
        srl = ''.join(KEY[n] for n in name)
        if srl == serial:
            names.append(name)

with open('namenum.out', 'w') as fout:
    if names:
        fout.write('\n'.join(names) + '\n')
    else:
        fout.write('NONE' + '\n')
