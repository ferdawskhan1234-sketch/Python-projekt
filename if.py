#Räkna hur många tal som är jämna och skriv samtidigt ut varje jämnt tal.

# tal = [4, 9, 2, 15, 7, 20, 6]
# count=0
# q=0
# while q < len(tal):
#     if tal[q]%2==0:
#         print(tal[q])

#         count+=1
#     q+=1
# print(count)


#Hitta det första talet som är större än 10 och skriv ut dess position (index)

# tal1 = [8, 3, 12, 5, 20, 7, 14]
# w=0
# första=tal1[w]
# while w < len(tal1):
#     if tal1[w]>10:
#         första=tal1[w]
#         första=w
#         break
#     w+=1
# print(första)


#Räkna summan av alla tal som är mindre än 10
# e=0
# somma=0
# tal2 = [5, 8, 13, 4, 17, 6]
# while e < len(tal2):
#     if tal2[e]<10:
#         somma+=tal2[e]
#     e+=1
# print(somma)

#Hitta det första talet som är mindre 
#än 5 och skriv ut både talet och dess index.
# tal3 = [ 4, 7, 12, 3, 18, 9, 25]
# r=0
# förstta=tal3[r]
# while r< len(tal3):
#     if tal3[r]<5:
#         förstta=tal3[r]
#         break
#     r+=1
# print(r)
# print(förstta)



#Räkna hur många tal som är jämna och samtidigt större än 5.

# tal4 = [8, 3, 14, 6, 21, 5, 10]
# t=0
# count=0
# while t < len(tal4):
#     if tal4[t]%2==0 and tal4[t]>5:
#         count+=1
#     t+=1
# print(count)


#Hitta det första talet som är udda och större än 10. Skriv ut talet.
# tal5 = [6, 13, 4, 18, 9, 21, 8]
# y=0
# udda=tal5[y]
# while y < len(tal5):
#     if tal5[y]%2==1 and tal5[y]>10:
#      udda=tal5[y]
#      break
#     y+=1
# print(udda)


#Gå igenom listan med while och räkna ut summan av 
#alla tal som finns på udda positioner (index).
# tal6 = [4, 9, 12, 3, 7, 15, 2]
# i=0
# summma=0
# uddda=tal6[i]
# while i < len(tal6):
#     if tal6[i]%2==1:
#         uddda=tal6[i]
#         summma+=tal6[i]
#     i+=1
# print(summma)



#Hitta det första talet som är 
#större än 10 och skriv ut både talet och dess index.
# tal7 = [8, 3, 14, 6, 21, 5, 10]
# o=0
# förstaa=0

# while o < len(tal7):
#    if tal7[o]>10:
#       förstaa=tal7[o]
#       break

#    o+=1
# print(förstaa)
# print(o)


#Räkna ut summan av
#talen från och med det första talet som är stötal
# tal8 = [5, 12, 8, 3, 17, 6, 10]
# p=0
# soomma=0
# while p < len(tal8):
#     if tal8[p]>10:
#         break
#     p+=1



#     while p <len(tal8):
#         soomma+=tal8[p]
#         p+=1
# print(soomma)


#Gå igenom listan med while.
#Hitta det största talet i listan och skriv ut både talet och dess index.
# tal9 = [7, 4, 15, 9, 22, 6, 11]

# å = 0
# största = tal9[å]
# ind = å

# while å < len(tal9):
#     if tal9[å] > största:
#         största = tal9[å]
#         ind = å
#     å += 1

# print(största)
# print(ind)


#Gå igenom listan med while.
#Räkna hur många tal som finns mellan 5 och 20, inklusive 5 och 20.

# tal10 = [3, 8, 14, 5, 19, 7, 22]
# a=0
# count=0
# while a < len(tal10):
#     if tal10[a]>=5 and tal10[a]<=20:
#         count+=1
#     a+=1
# print(count)    





#Gå igenom listan med while.
#Räkna summan av talen som står före 18.

# tal11 = [6, 11, 4, 18, 9, 25, 7]
# s= 0
# suuma=0
# while s< len(tal11):
#     if tal11[s]<18:
#         suuma+=tal11[s]
#     s+=1
# print(suuma)


#Hitta det första talet som är mindre än 10 och 
#skriv ut både talet och dess index.

# tal12 = [4, 9, 2, 16, 7, 13, 5]
# d=0
# mindre=0
# index=d
# while d < len(tal12):
#     if tal12[d]<10:
#         mindre=tal12[d]
#         index=d
#         break
#     d+=1
# print(mindre)
# print(index)

#Gå igenom listan med while.
#Räkna hur många tal som är större än 5 och mindre än 15.

# tal13 = [8, 3, 15, 6, 12, 4, 19]
# f=0
# count=0
# while f < len(tal13):
#     if tal13[f]>5 and tal13[f]<15:
#         count+=1
#     f+=1
# print(count)


#Hitta det sista talet som är mindre 
#än 10 och skriv ut både talet och dess index.

# tal14 = [5, 12, 7, 18, 3, 21, 9]
# g=0
# sistatal=tal14[g]
# indexx=0
# while g < len(tal14):
#     if tal14[g]<10:
#         sistatal=tal14[g]
#         indexx=g
#     g+=1
# print(indexx)
# print(sistatal)



#Gå igenom listan med while.
#Räkna ut summan av alla tal på jämna index (0, 2, 4, 6).

# tal15 = [4, 11, 7, 16, 3, 20, 9]
# h=0
# summan=0

# while h < len(tal15):
#     if h%2==0:
#         summan+=tal15[h]
#     h+=1
# print(summan)




#Byt ut alla tal som är större än 10 mot 0.

# tal16 = [7, 14, 3, 9, 18, 5, 11]
# j=0
# while j < len(tal16):
#     if tal16[j]>10:
#         tal16[j]=0
#     j+=1
# print(tal16)



#Gå igenom listan med while.
#Hitta det minsta talet i listan och skriv ut både talet och dess index.
# tal17 = [4, 8, 15, 3, 12, 7, 20]
# k=0
# minst=tal17[k]
# pos=0
# while k < len(tal17):
#     if tal17[k]<minst:
#         minst=tal17[k]
#         pos=k
#     k+=1
# print(pos)
# print(minst)



#Gå igenom listan med while.
#Räkna hur många tal som är större än 8.
# tal18 = [6, 13, 4, 18, 9, 21, 8]
# l=0
# count=0
# while l < len(tal18):
#     if tal18[l]>8:
#         count+=1
#     l+=1
# print(count)




#Gå igenom listan med while.
#Räkna ut summan av alla tal på udda index.

# talt19= [5, 12, 7, 4, 18, 9, 20]
# ö=0
# sooma=0
# while ö < len(talt19):
#     if ö %2==1:
#         sooma+=talt19[ö]
#     ö+=1
# print(sooma)

#Byt plats på det första och det sista talet.
# tal20 = [10, 4, 7, 13, 20, 8]
# ä=0
# while ä < len(tal20):
#     första=tal20[0]
#     tal20[0]=tal20[-1]
#     tal20[-1]=första
#     break

# ä+=1
# print(tal20)



#Byt plats på det andra och det femte talet.
# tal20 = [6, 12, 4, 9, 15, 21]
# z=0
# while z < len(tal20):
#     andra=tal20[1]
#     tal20[1]=tal20[4]
#     tal20[4]=andra
#     break
# z+=1
# print(tal20)



#Byt plats på det tredje och det sjätte talet.
# tal23 = [8, 3, 14, 6, 19, 11]
# x=0
# while x < len(tal23):
#     tredje=tal23[2]
#     tal23[2]=tal23[5]
#     tal23[5]=tredje
#     break
# x+=1
# print(tal23)

#Gå igenom listan med while.

#Hitta det första talet som är större än 10 och
#skriv ut summan av alla tal före det talet.

# tal24 = [7, 12, 4, 18, 9, 15, 6]
# c = 0
# ssomma = 0
# while c < len(tal24):
#     if tal24[c] > 10:
#         break

#     ssomma += tal24[c]
#     c += 1

# print(ssomma)




#Räkna hur många tal som är mindre än 15 och samtidigt jämna.

tal31 = [6, 14, 3, 9, 18, 5, 11]
v=0
count=0
while v < len(tal31):
    if tal31[v]<15 and tal31[v]%2==0:
        count+=1

    v+=1
print(count)















































































































































