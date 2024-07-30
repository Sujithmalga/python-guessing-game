def ciphertex(n,k):
    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    list2 = []
    list3 = []
    str1  = ""
    for i in n:
        if i in list1:
            list2.append(i)
    for j in list2:
       x =  list1.index(j)
       x = x +k
       s = list1[x]
       list3.append(s)
    for v in  list3:
        str1 += v 
    return str1


n = input("enter the plain text")
k = int(input("enter the key num"))
var  = ciphertex(n,k)
print(var)

    