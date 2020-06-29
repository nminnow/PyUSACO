'''
ID: audrey.6
LANG: PYTHON3
PROB: crypt1
'''

with open('crypt1.in') as fin:
    l = int(next(fin).rstrip())
    digits = next(fin).rstrip().split()

ans = 0
for i in range(100, 1000):
    if all(d in digits for d in str(i)):
        for j in range(10, 100):
            a, b = str(j)
            if a in digits and b in digits:
                p = int(a) * i
                if all(d in digits for d in str(p)) and len(str(p)) == 3:
                    q = int(b) * i
                    if all(d in digits for d in str(q)) and len(str(q)) == 3:
                        x = p * 10 + q
                        if all(d in digits for d in str(x)) and len(str(x)) == 4:
                            print(i, j, x)
                            ans += 1

with open('crypt1.out', 'w') as fout:
    fout.write(f'{ans}\n')
