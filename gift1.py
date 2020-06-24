'''
ID: audrey.6
LANG: PYTHON3
PROG: gift1
'''

with open('gift1.in') as f:
    persons = {}
    for _ in range(int(next(f).rstrip())):
        persons[next(f).rstrip()] = 0

    for _ in range(len(persons)):
        person = next(f).rstrip()
        g, r = map(int, next(f).split())

        if r != 0:
            persons[person] += g % r - g
            m = g // r

            for q in range(r):
                persons[next(f).rstrip()] += m

with open('gift1.out', 'w') as f:
    for person in persons:
        f.write(person + ' ' + str(persons[person]) + '\n')
