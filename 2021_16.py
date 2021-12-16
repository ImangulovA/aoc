
import copy

hexadeci = """0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111""".splitlines()

dicth = {}
for h in hexadeci:
    a = h.split(' = ')
    dicth[a[0]] = a[1]

inp = open('Downloads/input.txt',mode='r').read().split('\n')
inp = [x for x in inp if x]
#print(inp)

inp = inp[0]

nstr = ''

for s in inp: 
    nstr += dicth[s]

def parsepacket(nstr,pntr=0):
    sumv = 0
    v = int(nstr[pntr:pntr+3],2)
    sumv+=v
    pntr += 3
    t = int(nstr[pntr:pntr+3],2)
    pntr += 3
    if t != 4:
        i = int(nstr[pntr],2)
        pntr += 1
        if i == 1:
            l = int(nstr[pntr:pntr+11],2)
            pntr += 11
        if i == 0:
            l = int(nstr[pntr:pntr+15],2)
            pntr += 15
        sp = []
        condtn = True
        opntr = copy.deepcopy(pntr)
        pc = 0
        digs = []
        while condtn:
            pntr,nv,dig = parsepacket(nstr,pntr)
            digs.append(dig)
            sumv+=nv
            if i == 1:
                pc+=1
                condtn = pc < l
            if i == 0:
                condtn = (pntr - opntr) < l
        if t == 7:
            answ = int(digs[0]==digs[1])
        elif t == 6:
            answ = int(digs[0]<digs[1])
        elif t == 5:
            answ = int(digs[0]>digs[1])
        elif t == 3:
            answ = max(digs)
        elif t == 2:
            answ = min(digs)
        elif t==1:
            answ = 1
            for d in digs:
                answ = answ * d
        elif t==0:
            answ = sum(digs)
        return pntr, sumv, answ        
    else: 
        readdig = 1
        sdigpart = ''
        while readdig:
            readdig = int(nstr[pntr],2)
            sdigpart += (nstr[pntr+1:pntr+5])
            pntr+=5
        sdigpart = int(sdigpart,2)
        return pntr,sumv, sdigpart

parsepacket(nstr)
