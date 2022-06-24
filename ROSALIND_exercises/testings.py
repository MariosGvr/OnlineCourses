#Certain Point Mutations are More Common




seq1=input("first seq: ")
seq2=input("second seq: ")
count=-1
tv=0
ts=0
for base1 in seq1:
    count+=1
    base2= seq2[count] 
    
    if base1 != base2:
        
        if (base1=='G' or base2=='G') and (base2=='A' or base1=='A'):
            ts += 1
        elif (base1=='C' or base2=='C') and (base2=='T' or base1=='T'):
            ts += 1
        else:
            tv += 1

print (ts/tv)