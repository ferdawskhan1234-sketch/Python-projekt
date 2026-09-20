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
# tal8 = [7, 14, 3, 18, 9, 22, 5]
# o=0

# index_första=0
# index_andra=0
# while o < len(tal8):
#     if tal8[o]>10:
#         index_första=o
#         break
        
#     o+=1
    

# while o < len(tal8):
#         if tal8[o]>10:
#             index_andra=o
#         o+=1

# print(index_första)
# print(index_andra)



#Gå igenom listan med while.
#Hitta det största udda talet och skriv ut både talet och dess index.
# tal10 = [8, 3, 14, 7, 20, 5, 12]
# p=0
# uddda=0
# iindex=0
# while p < len(tal10):
#     if tal10[p]>uddda and tal10[p]%2==1:
#         uddda=tal10[p]
#         iindex=p
        
        
#     p+=1
# print(uddda)
# print(iindex)



#Gå igenom listan med while.
#Hitta det minsta udda talet och skriv ut både talet och dess index.

# tal11 = [9, 4, 16, 7, 12, 3, 20]
# å=0
# minsta=tal11[å]
# inndex=0
# while å < len(tal11):
#     if tal11[å]<minsta and tal11[å]%2==1:
#         minsta=tal11[å]
#         inndex=å
        
#     å+=1
# print(minsta)
# print(inndex)


#Gå igenom listan med while.
#Hitta det första udda talet och byt ut det mot 0.

# tal12 = [6, 13, 4, 18, 7, 21, 9]
# a=0
# uuda=0
# while a < len(tal12):
#     if tal12[a]%2==1:
#         uuda=tal12[a]=0
#         break
#     a+=1
# print(tal12)



#Gå igenom listan med while och skriv ut index och 
#värde för varje element.


# tal13 = [6, 13, 4, 18, 7, 21, 9]
# s=0
# while s < len(tal13):

#   print(s, tal13[s])
#   s+=1


#Gå igenom listan med while och skriv ut bara värdet på varje element.
# tal14 = [10, 5, 8, 14, 3]
# d=0
# while d < len(tal14):
#     print(tal14[d])
#     d+=1


#Gå igenom listan med while och skriv ut indexet och värdet,
# men bara för index 0, 2 och 4.

# tal15 = [10, 5, 8, 14, 3]
# f = 0
# while f < len(tal15):
#     if f % 2 == 0:
#         print(f, tal15[f])
#     f += 1



#Gå igenom listan med while.
#Skriv ut index och värde för varje tal som är större än 10.

# tal16 = [8, 5, 12, 3, 16]
# g=0
# while g < len(tal16):
#     if tal16[g]>10:
#         print(g, tal16[g])
#     g+=1



#Gå igenom listan med while.

#Skriv ut index och värde för varje tal som är större än 10.
# tal17 = [7, 12, 4, 18, 9, 6]
# h=0
# while h < len(tal17):
#     if tal17[h]>10:
#         print(h, tal17[h])
#     h+=1





#Gå igenom listan med while.
#Skriv ut index och värde för varje jämnt tal.

# tal18 = [4, 11, 7, 16, 3, 20]
# j=0
# while j < len (tal18):
#     if tal18[j]%2==0:
#         print(j, tal18[j])
#     j+=1


#Skriv ut index och värde för varje tal som 
#är både jämnt och större än 10.
# tal19 = [9, 4, 13, 6, 18, 5]
# l=0
# while l < len(tal19):
#     if tal19[l]%2==0 and tal19[l]>10:
#         print(l, tal19[l])
#     l+=1




#Gå igenom listan med while.
#Skriv ut index och värde för varje tal som är udda och mindre än 20.

# tal20 = [6, 13, 8, 21, 4, 16]
# ö=0
# while ö < len(tal20):
#     if tal20[ö]%2==1 and tal20[ö]<20:
#         print(ö, tal20[ö])
#     ö+=1


#Gå igenom listan med while.
#Skriv ut index och värde för varje tal som är mindre än 10.
#tal21 = [7, 12, 5, 18, 9, 4]
# ä=0
# while ä < len(tal21):
#     if tal21[ä]<10:
#         print(ä, tal21[ä])
#     ä+=1


#Gå igenom listan med while.
#Skriv ut index och värde för varje tal som är större än 10 och udda
# tal22= [4, 15, 8, 21, 6, 13]
# z=0
# while z < len(tal22):
#     if tal22[z]>10 and tal22[z]%2==1:
#         print(z, tal22[z])
#     z+=1


#Gå igenom listan med while.
#Skriv ut index och värde för varje tal som är jämnt och mindre än 15.

# tal23 = [8, 3, 14, 7, 20, 5]
# x=0
# while x < len(tal23):
#     if tal23[x]%2==0 and tal23[x]<15:
#         print(x, tal23[x])
#     x+=1


#Skriv ut index och värde för det första talet
#som är både jämnt och större än 10

tal24 = [5, 12, 7, 18, 4, 21]
c=0

while c < len(tal24):
    if tal24[c]>10 and tal24[c]%2==0:
     break
    c+=1

        

print( c, tal24[c])
    












































































    





























