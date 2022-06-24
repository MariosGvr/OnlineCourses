



sequences = []

sequence=""
data=input()
sequences=[]
for i in data:
    if i in ">Rosalind_1234567890":
        if i==">":
            sequences.append(sequence)
            sequence= ""
        continue
    if i != "\n":
        sequence+=i   

sequences = sequences[1:]

count = 0
listA = ["A:"]
listG = ["G:"]
listC = ["C:"]
listT = ["T:"]

NumOfVal = len(sequences[0])

for time in range(NumOfVal):
    listA.append(0)
    listG.append(0)
    listC.append(0)
    listT.append(0)
    

for sequence in sequences:
    for base in sequence:
        count +=1
        if base == "A":
            listA[count] = listA[count] + 1
        if base == "G":
            
            listG[count] = listG[count] + 1
        if base == "C":
            listC[count] = listC[count] + 1
        if base == "T":
            listT[count] = listT[count] + 1
    count = 0


final = ""
for i in range(NumOfVal):
    if max(listA[i+1],listG[i+1],listC[i+1],listT[i+1]) == listA[i+1]:
        final += "A"
        continue
    if max(listA[i+1],listG[i+1],listC[i+1],listT[i+1]) == listG[i+1]:
        final += "G"
        continue
    if max(listA[i+1],listG[i+1],listC[i+1],listT[i+1]) == listC[i+1]:
        final += "C"
        continue
    if max(listA[i+1],listG[i+1],listC[i+1],listT[i+1]) == listT[i+1]:
        final +="T"
        continue
print(final)
stringA=""
for i in listA:
    stringA += (str(i) +" ")
print(stringA)

stringC=""
for i in listC:
    stringC += (str(i) +" ")
print(stringC)

stringG=""
for i in listG:
    stringG += (str(i) +" ")
print(stringG)

stringT=""
for i in listT:
    stringT += (str(i) +" ")
print(stringT)
