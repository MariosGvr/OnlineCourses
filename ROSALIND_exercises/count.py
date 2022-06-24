

pack=[]
list_num=[1,2,3]
def package (list_num, pack):
    if len(list_num) == len (pack):
        print (pack)
        
        #print ("hiii")
    else:
        for i in list_num:
            if i not in pack:
                pack.append(i)
            for j in list_num:
                #print (i, "aaa")
                if j != i and j not in pack:
                    #print ("boom")
                    pack.append(j)
                    #print (pack)
                    package(list_num,pack)
            pack=[]
            
package(list_num,pack)