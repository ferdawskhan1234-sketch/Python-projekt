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

# tal31 = [6, 14, 3, 9, 18, 5, 11]
# v=0
# count=0
# while v < len(tal31):
#     if tal31[v]<15 and tal31[v]%2==0:
#         count+=1

#     v+=1
# print(count)


#Räkna ut summan av alla tal som är större än 8.
# tal43 = [7, 12, 5, 18, 3, 10]
# b=0
# summa=0
# while b < len(tal43):
#     if tal43[b]>8:
#         summa+=tal43[b]
#     b+=1
# print(summa)




#Räkna hur många tal som är udda.
# tal44 = [6, 15, 4, 21, 8, 13]
# n=0
# count=0
# while n < len(tal44):
#     if tal44[n]%2==1:
#         count+=1
#     n+=1
# print(count)





#Hitta det minsta udda talet i listan.

# tal45 = [8, 3, 14, 7, 20, 5]
# m=0
# minsta=tal45[m]
# while m < len(tal45):
#     if tal45[m]<minsta and tal45[m]%2==1:
#         minsta=tal45[m]
#     m+=1
# print(minsta)



#Räkna ut medelvärdet av alla tal i listan.
# tal46 = [4, 11, 8, 15, 6, 20]
# qq=0
# summa=0
# count=0
# medel=0
# while qq < len(tal46):
#     count+=1
#     summa+=tal46[qq]
#     medel=summa/count
#     qq+=1
# print(medel)



#Räkna ut summan av alla tal som är mindre än 10.
# tal47 = [5, 12, 8, 3, 17, 6]
# ww=0
# somma=0
# while ww < len(tal47):
#     if tal47[ww]<10:
#         somma+=tal47[ww]
#     ww+=1
# print(somma)





#Räkna hur många tal som är jämna.
# tal48 = [7, 14, 3, 18, 9, 12]
# ee=0
# count=0
# while ee < len(tal48):
#     if tal48[ee]%2==0:
#         count+=1
#     ee+=1
# print(count)





#Hitta det största talet som är mindre än 16.

# tal49 = [6, 13, 4, 21, 8, 15]
# rr=0
# mindre=tal49[rr]
# while rr < len(tal49):
#     if tal49[rr]<16 and tal49 and tal49[rr]>mindre:
#         mindre=tal49[rr]
        
#     rr+=1
# print(mindre)


#Hitta det minsta talet som är större än 5.
# tal50 = [9, 4, 17, 6, 12, 3]
# tt=0
# minstta=tal50[tt]
# while tt < len(tal50):
#     if tal50[tt]>5 and tal50[tt]<minstta:
#         minstta=tal50[tt]
#     tt+=1
# print(minstta)




#Skriv ut alla tal som är större än 10.
# tal = [5, 10, 15, 20, 25]

# for x in tal:
#   if x >10:
#     print(x)

#Skriv ut alla jämna tal.
# tal1 = [4, 7, 12, 9, 16, 3]
# for z in tal1:
#     if z %2==0:
#         print(z) 



# #Räkna summan av alla tal som är större än 10.
# tal2 = [5, 12, 8, 3, 17, 6]
# somma=0
# for ä in tal2:
#     if ä >10:
#         somma+=ä
# print(somma)


# #Räkna hur många tal som är udda.

# tal3 = [8, 13, 4, 21, 6, 15]
# count=0
# for ö in tal3:
#     if ö %2==1:
#         count+=1
# print(count)
    

#Hitta det största talet i listan.
# tal4 = [7, 14, 3, 18, 9, 22]
# stösta=0
# for l in tal4:
#     if l >stösta:
#         stösta+=l
# print(l)

#Ändra alla jämna tal så att de blir dubbelt så stora.

# tal5 = [4, 7, 12, 9, 16, 3]
# for k in range(len(tal5)):
#     if tal5[k]%2==0:
#         tal5[k]=tal5[k]*2
# print(tal5)

# #Ändra alla tal som är större än 10 till 0.

# tal6 = [5, 12, 7, 18, 4, 21]
# for j in range(len(tal6)):
#     if tal6[j]>10:
#         tal6[j]=0
# print(tal6)



#Ändra alla tal som är mindre än 10 till 100.
# tal7 = [4, 9, 12, 7, 16, 3]
# for h in range(len(tal7)):
#     if tal7[h]<10:
#         tal7[h]=100
# print(tal7)


#Byt plats på det första och sista talet.

# tal8 = [5, 12, 7, 18, 4, 21]
# for g in range(len(tal8)):
#     one=tal8[0]
#     tal8[0]=tal8[-1]
#     tal8[-1]=one
#     break
# print(tal8)



#Byt plats på det andra och det femte talet.

# tal9 = [8, 3, 14, 6, 19, 11]
# for f in range(len(tal9)):
#     andra=tal9[1]
#     tal9[1]=tal9[-2]
#     tal9[-2]=andra
#     break
# print(tal9)


#Byt plats på det tredje och det sjätte talet.
# tal10 = [7, 12, 4, 18, 9, 21]
# for d in range(len(tal10)):
#     tredje=tal10[2]
#     tal10[2]=tal10[-1]
#     tal10[-1]=tredje
#     break
# print(tal10)


#Skapa en ny lista som innehåller bara de tal som är större än 10.
# tal11 = [4, 7, 12, 3, 18, 9]
# tal12=[]
# for s in range(len(tal11)):
#     if tal11[s]>10:
        
#         tal12.append(tal11[s])
# print(tal12)


#Skapa en ny lista som innehåller alla jämna tal från tal12.
# tal12 = [5, 14, 8, 21, 3, 16]
# q=[]
# for a in range(len(tal12)):
#     if tal12[a]%2==0:
#         q.append(tal12[a])
# print(q)



#Skapa en ny lista som innehåller alla tal som är mindre än 10.
# tal13 = [6, 15, 4, 9, 18, 7]
# w=[]
# for e in range(len(tal13)):
#     if tal13[e]<10:
#         w.append(tal13[e])
# print(w)

#Skapa en ny lista som innehåller talen från tal14, men där varje tal som 
#är större än 10 ersätts med 0.
# tal14 = [5, 12, 7, 18, 4, 21]
# w=[]
# for r in range(len(tal14)):
#     if tal14[r]>10:
#         w.append(0)
#     else:
#         w.append(tal14[r])
# print(w)


#Skapa en ny lista som innehåller varje tal
#från tal15, men dubbla varje tal.
# tal15 = [4, 7, 12, 3, 18, 9]
# t=[]
# for y in range(len(tal15)):
       
#         t.append(tal15[y]*2)
# print(t)




#tal större än 10 blir dubblerade
#tal 10 eller mindre lämnas som de är
# tal16 = [5, 12, 7, 18, 4, 21]
# u=[]
# for a in range(len(tal16)):
#     if tal16[a]>10:
#         u.append(tal16[a]*2)
#     else:
#         u.append(tal16[a])
# print(u)



#Skapa en ny lista där:jämna tal blir 0
# udda tal lämnas som de är
# tal17 = [4, 11, 8, 15, 6, 20]
# i=[]
# for d in range(len(tal17)):
#     if tal17[d]%2==0:
#         i.append(0)
#     else:
#         i.append(tal17[d])
# print(i)

#Skapa en ny lista där: tal större än 10 blir 100
#tal 10 eller mindre blir 0
# tal18 = [6, 13, 4, 17, 8, 21]
# o=[]
# for f in range(len(tal18)):
#     if tal18[f]>10:
#         o.append(100)
#     elif tal18[f]<10:
#         o.append(0)
#     else:
#         o.append(tal18[f])
# print(o)


#Skapa en ny lista där:jämna tal blir dubblerade
#udda tal blir 0
# tal19 = [4, 13, 8, 17, 6, 21]
# p=[]
# for g in range(len(tal19)):
#     if tal19[g]%2==0:
#         p.append(tal19[g]*2)
#     elif tal19[g]%2==1:
#         p.append(0)
# print(p)


#Skapa en ny lista där: tal mindre än 10 blir tal * 2
#tal 10 eller större blir tal - 5
# tal20 = [7, 12, 5, 18, 3, 14]
# å=[]
# for h in range(len(tal20)):
#     if tal20[h]<10:
#         å.append(tal20[h]*2)
#     elif tal20[h]>10:
#         å.append(tal20[h]-5)
# print(å)

#Skapa en ny lista där:tal som är mindre än 10 blir 0
#tal mellan 10 och 20 blir dubblerade:tal som är större än 20 blir 100

# tal21 = [4, 15, 8, 21, 6, 13]
# a=[]
# for j in range(len(tal21)):
#     if tal21[j]>10 and tal21[j]<20:
#         a.append(tal21[j]*2)
#     elif tal21[j]<10:
#         a.append(0)
#     elif tal21[j]>20:
#         a.append(100)
# print(a)


#Skapa en ny lista där:jämna tal blir tal + 1: udda tal blir tal - 1
# tal22 = [6, 14, 3, 19, 8, 22]
# s=[]
# for k in range(len(tal22)):
#     if tal22[k]%2==0:
#         s.append(tal22[k]+1)
#     elif tal22[k]%2==1:
#         s.append(tal22[k]-1)
# print(s)

#Skapa en ny lista där:
# tal mindre än 10 → tal + 5
# tal mellan 10 och 20 → tal - 2
#tal större än 20 → tal * 2
# tal23 = [5, 12, 7, 18, 4, 21]
# d=[]
# for l in range(len(tal23)):
#     if tal23[l]>10 and tal23[l]<20:
#         d.append(tal23[l]-2)
#     elif tal23[l]<10:
#         d.append(tal23[l]+5)
#     elif tal23[l]>20:
#         d.append(tal23[l]*2)
# print(d)

#Skapa en ny lista där:
#jämna tal → tal / 2
#udda tal → tal * 3
# tal24 = [8, 13, 4, 17, 6, 21]
# f=[]
# for ö in range(len(tal24)):
#     if tal24[ö]%2==0:
#         f.append(tal24[ö]/2)
#     elif tal24[ö]%2==1:
#         f.append(tal24[ö]*3)
# print(f)

#Skapa en ny lista som innehåller talen i omvänd ordning.
# tal25 = [4, 7, 12, 3, 18, 9]
# g=[]
# for ä in range(len(tal25)-1,-1,-1):
#         g.append(tal25[ä])
# print(g)



#Skapa en ny lista som innehåller bara de tal som är
# större än 5, men i omvänd ordning.
# tal26 = [4, 7, 12, 3, 18, 9]
# h=[]
# for z in range(len(tal26)-1,-1,-1):
#     if tal26[z]>5:
#       h.append(tal26[z])
# print(h)

#Skapa en ny lista med alla tal
#som är udda, men lägg dem i omvänd ordning.
# tal27 = [6, 15, 4, 21, 8, 13]
# j=[]
# for x in range(len(tal27)-1,-1,-1):
#     if tal27[x]%2==1:
#         j.append(tal27[x])
# print(j)

































































































































































