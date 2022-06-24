data= input()
subseq=""
seq_list= []

lenght=0
seq_len= {}
count=0
finalseq=""

for i in data:
    if i in ">Rosalind_1234567890":
        if i==">":
            seq_list.append(finalseq)
            finalseq= ""
        continue
    if i != "\n":
        finalseq+=i    
        
        


del seq_list[0]
allofem= len(seq_list)
seq1 = seq_list[0]

while len(seq1)>1:
    for base in seq1:
        subseq += base
        if len(subseq)>=2:
            for sequence in seq_list:
                if subseq not in sequence:
                    count=0
                    break
                else:
                    count += 1
                    if count == allofem:
                        lenght = len(subseq)
                        seq_len[subseq]=lenght
                        count = 0
                        break
    seq1 = seq1[1:]
    subseq= ""

print(max(zip(seq_len.values(), seq_len.keys())))
