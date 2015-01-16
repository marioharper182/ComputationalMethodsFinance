__author__ = 'mario'

clst = [6, 9, 20]

dumplist = [clst[0]*x+clst[1]*y+clst[2]*z for x in range(0,40) for y in range(0, 30) for z in range(0, 15)]
set = list(set(dumplist))
keyvalues = [set[x] for x in range(1,(len(set)-1)) if set[x]+1 != set[x+1] and set[x]<100]

answer = [max(keyvalues)+1]
print("The highest integer of chicken nuggets puchaseable is:", answer[0])