p_n=list()
#creat the list
p_n+=[2]
p_n+=[3]
i=3
l=1
#list's and variables's intialize
while i<=100:
    i+=2
    k=0
    j=0
    while k<len(p_n)-1:
        if i%p_n[k]!=0:
            j+=1
        k+=1
    if j==len(p_n)-1:# test to prime number
        p_n+=[i]# add list
    print(i)
print(p_n)
print(p_n[-1])
print(len(p_n))
print("****")
