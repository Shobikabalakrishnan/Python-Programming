l1 = [1,3,4]
l2 = [2,8,9]
l3 = [6,2,9]
l = [l1,l2,l3]
for i in l:
    print("[",end=' ')  
    for j in i:
        print(j,end=" ")
    print("]")  
    print(end="\n")  