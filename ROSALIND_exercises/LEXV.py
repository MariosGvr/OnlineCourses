
letters= input("place your input here: ")
letter_list=letters.split(" ")
seq=[]
num =int(input("the length is: "))

def lex (leter_list,seq):
    if num==len (seq):
        print ('',end="")
    else:
        for i in letter_list:
                seq.append(i)
                print (''.join(seq))
                lex(letter_list,seq)
                seq.pop()

lex(letter_list,seq)