path=['n','e','s','e','s','e','c']

l=len(path)
def match(li,i,j,c):
   # print("Inside this function")
    if j+c >= len(li):
        return li
    flg=0
    ji=j
    for k in range(c):
        if li[i]!=li[j]:
            flg=1
            return li
        i=i+1
        j=j+1
    if flg==0:
        print("There exists a loop and trimming it")
        for k in range(c):
            li[ji]='*'
            ji=ji+1
    return li
            
        
def eliminateloop(lis):
    for j in range(1,l):
        for i in range(j-1,-1,-1):
            #print("the value of j is ",lis[j]," the value of j is ",lis[i])
            if lis[j]==lis[i]:
                lis=match(lis,i,j,j-1)
                #print("the value of j is ",lis[j]," the value of j is ",lis[i])
    return lis
                
                
path=eliminateloop(path)
print(path)