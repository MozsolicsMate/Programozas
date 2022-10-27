szavak = ["fekete", "sötét", "afroamerikai", "néger", "Zimbabwei"]

maxindex = 0
maxertek = szavak[0]

for i in range(len(szavak)):
    c = 0
    for k in range(len(szavak[i])):
        c += 1
    if c > len(szavak[i]):
        maxertek = szavak[i]
        maxindex = i

print(f"A leghosszabb szó: {maxertek}, ami {maxindex + 1}-ik a listában")

#nem jó :\