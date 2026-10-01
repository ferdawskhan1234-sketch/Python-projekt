#Skapa en ny lista där:tal som är jämna → dubbleras
#tal som är udda → blir 0
# tal1 = [6, 15, 4, 21, 8, 13]
# m=[]
# for q in range(len(tal1)):
#     if tal1[q]%2==0:
#         m.append(tal1[q]*2)
#     elif tal1[q]%2==1:
#         m.append(0)
# print(m)

#Skapa en ny lista där:tal mindre än 10 → tal + 1
#tal 10 eller större → tal - 1
# tal2 = [7, 12, 5, 18, 9, 21]
# n=[]
# for w in range(len(tal2)):
#     if tal2[w]<10:
#         n.append(tal2[w]+1)
#     elif tal2[w]>10:
#         n.append(tal2[w]-1)
#print(n)

#Skapa en ny lista som innehåller:tal som är jämna → tal + 10
#tal som är udda → tal - 1
# tal3 = [4, 11, 8, 17, 6, 21]
# b=[]
# for e in range(len(tal3)):
#     if tal3[e]%2==0:
#         b.append(tal3[e]+10)
#     elif tal3[e]%2==1:
#         b.append(tal3[e]-1)
# print(b)

#Hitta indexet för talet 19.
# tal4 = [8, 14, 5, 19, 7, 12]
# index=0
# for r in range(len(tal4)):
#     if tal4[r]==19:
#         index=r

# print(index)

#Räkna ut hur många gånger talet 7 finns i listan.
# tal5 = [4, 7, 12, 7, 18, 7]
# count=0
# for t in range(len(tal5)):
#     if tal5[t]==7:
#         count+=1
# print(count)


#Hitta indexet för det första talet som är större än 10.
# tal6 = [4, 9, 12, 3, 18, 7]
# inndex=0
# for y in range(len(tal6)):
#     if tal6[y]>10:
#         inndex=y
#         break
# print(inndex)

#Hitta det sista indexet där talet är 8.
# tal7 = [4, 8, 15, 8, 12, 8]
# iindex=0
# for u in range(len(tal7)):
#     if tal7[u]==8:
#         iindex=u
# print(iindex)


#Räkna ut summan av talen från och
#med det första talet som är större än 10.
# tal8 = [4, 7, 12, 3, 18, 9]
# summa=0
# inddex=0
# for i in range(len(tal8)):
#     if tal8[i]>10:
#        inddex=i
#        break
       

# for i in range(inddex,len(tal8)):
#       summa+=tal8[i]
# print(summa)

#Hitta indexet för det största talet.
# tal9 = [8, 13, 5, 21, 7, 16]

# största = tal9[0]
# index = 0

# for o in range(len(tal9)):
#     if tal9[o] > största:
#         största = tal9[o]
#         index = o

# print(index)

#Skapa en ny lista som innehåller bara talen som är större än 10,
# men varje sådant tal ska minskas med 2.

# tal10 = [8, 4, 15, 7, 12, 3, 18]
# m=[]
# c=0
# for p in range(len(tal10)):
#     if tal10[p]>10:
#         m.append(tal10[p]-2)
# print(m)




#Skapa en ny lista där: tal mindre än 10 blir 0
#tal från 10 och uppåt blir talet × 2

# tal11 = [5, 12, 7, 20, 9, 14]
# n=[]
# for å in range(len(tal11)):
#     if tal11[å]<10:
#         n.append(0)
#     elif tal11[å]>10:
#         n.append(tal11[å]*2)
# print(n)





#Skapa en ny lista där: jämna tal → delas med 2
#udda tal → multipliceras med 3
# tal12 = [4, 11, 8, 17, 6, 13, 20]
# b=[]
# for a in range(len(tal12)):
#     if tal12[a]%2==0:
#         b.append(tal12[a]//2)
#     elif tal12[a]%2==1:
#         b.append(tal12[a]*3)
# print(b)


#Skapa en ny lista där:tal mindre än 10 → lägg till talet + 5
#tal mellan 10 och 20 → lägg till talet - 3
#tal större än 20 → lägg till talet × 2
# tal13 = [7, 14, 3, 18, 9, 22, 5]
# v=[]
# for s in range(len(tal13)):
#     if tal13[s]>10 and tal13[s]<20:
#         v.append(tal13[s]-3)
#     elif tal13[s]<10:
#         v.append(tal13[s]+5)
#     elif tal13[s]>20:
#         v.append(tal13[s]*2)
# print(v)





































































