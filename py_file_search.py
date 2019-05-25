
try:
    fhand = open('mbox-short.txt')
except:
    print('Bad File')
    exit()
count = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        pos = line.find(':')
        num = float(line[pos+1:])
        count += 1
        print(num)

print(count)
