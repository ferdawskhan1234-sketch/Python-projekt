#Hitta det största jämna talet i listan 
#och skriv ut både talet och dess index.
# tal = [8, 3, 15, 6, 12, 4, 19]
# q = 0
# index=0
# största=tal[q]
# while q < len(tal):
#     if tal[q]>största and tal[q]%2==0:
#         största=tal[q]
#         index=q
#     q+=1
# print(index)
# print(största)



#Hitta det första talet som är större än 10 och jämnt. 
#Skriv ut både talet och dess index.

# tal1 = [5, 12, 7, 18, 4, 21, 9]
# w =0
# iindex=0
# jämnt=tal1[w]
# while w < len(tal1):
#     if tal1[w]>10 and tal1[w] %2==0:
#         jämnt=tal1[w]
#         iindex=w
#         break
#     w+=1
# print(jämnt)
# print(iindex)




# #Gå igenom listan med while.
# #Räkna ut summan av alla jämna tal som är mindre än 15.

# tal2 = [8, 3, 14, 6, 19, 11, 4]
# e=0
# suuma=0
# while e < len(tal2):
#     if tal2[e]%2==0 and tal2[e]<15:
#         suuma+=tal2[e]
#     e+=1
# print(suuma)

#Gå igenom listan med while.
#Hitta det sista jämna talet och skriv ut både talet och dess index.


# tal3 = [9, 4, 16, 7, 12, 3, 20]
# r=0
# ind=0
# sista=tal3[r]
# while r < len(tal3):
#     if tal3[r]%2==0:
#         sista=tal3[r]
#         ind=r
#     r+=1
# print(sista)
# print(ind)

#Gå igenom listan med while.
#Byt ut det första talet som är större än 10 mot 0.
# tal4 = [7, 4, 13, 8, 21, 6, 10]
# t=0
# försttaa=tal4[t]
# while t < len(tal4):
#     if tal4[t]>10:
#         försttaa=tal4[t]=0
#         break
#     t+=1
# print(tal4)









#Gå igenom listan med while.
#Hitta det första talet som är större än 10 och 
#byt plats på det med det sista talet.
# tal5 = [6, 11, 4, 18, 7, 15, 9]
# y=0
# sstöre=tal5[y]
# while y < len(tal5):
#      if tal5[y]>10:
#          sstöre=tal5[y]
#          break
#      y+=1

# while y < len(tal5):
      
#          fösta=tal5[1]
#          tal5[1]=tal5[-1]
#          tal5[-1]=fösta
#          break
# y+=1
# print(tal5)


#Hitta det första talet som är större än 10 och byt ut det mot 0.

# tal6 = [4, 9, 12, 7, 18, 5, 21]
# u=0
# bytmot=tal6[u]
# while u < len(tal6):
#     if tal6[u]>10:
#         bytmot=tal6[u]=0
#         break
#     u+=1
# print(tal6)


#Gå igenom listan med while.
#Hitta det sista talet som är större än 10 och
#skriv ut både talet och dess index.

# tal7 = [8, 5, 14, 3, 11, 6, 20]
# i=0
# sista=tal7[i]
# inddex=0
# while i < len(tal7):
#     if tal7[i]>10:
#         sista=tal7[i]
#         inddex=i
#     i+=1
# print(sista)
# print(inddex)


#Gå igenom listan med while.
#Hitta det första talet som är större än 10 och det sista
#talet som är större än 10. Skriv ut deras index.
tal8 = [7, 14, 3, 18, 9, 22, 5]
o=0

index_första=0
index_andra=0
while o < len(tal8):
    if tal8[o]>10:
        index_första=o
        break
        
    o+=1
    

while o < len(tal8):
        if tal8[o]>10:
            index_andra=o
        o+=1
print(index_första)
print(index_andra)




    





























