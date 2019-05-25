
try:
    fhand = open('mbox-short.txt')
except:
    print('Bad File')
    exit()

print(fhand)
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find(':')
        num = float(line[pos+1:])

        print(num)
