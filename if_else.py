# tal = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
# jämna=[]
# udda=[]
# for q in tal:
#     if q %2==0:
#         jämna.append(q)
#     else:
#         udda.append(q)
# print(udda)
# print(jämna)

# tal1 = [3, 8, 12, 15, 17, 20, 21, 25, 30]
# tre=[]
# fem=[]
# andra=[]
# for w in tal1:
#     if w %3==0:
#         tre.append(w)
#     elif w %5==0:
#         fem.append(w)
#     else:
#         andra.append(w)
# print(tre)
# print(fem)
# print(andra)


# tal2 = [3, 5, 9, 10, 12, 15, 18, 20, 25, 30, 31]
# båda=[]
# tree=[]
# övriga=[]
# for e in tal2:
#     if e %3==0 and e %5==0:
#         båda.append(e)
#     elif e %3==0 and  not e %5==0:
#         tree.append(e)
#     else:
#         övriga.append(e)
# print(båda)
# print(tree)
# print(övriga)


# namn1 = ["Ali", "Sara", "Omar", "Lina", "Alexander", "Eva", "Mohammad"]
# korta=[]
# mellan=[]
# långa=[]
# for r in namn1:
#     if len(r)<=3:
#         korta.append(r)
#     elif len(r) <=5:
#         mellan.append(r)
#     else:
#         långa.append(r)
# print(korta)
# print(mellan)
# print(långa)

# namn2 = ["Ali", "Sara", "Omar", "Adam", "Lina", "Alexander", "Eva"]
# börja=[]
# for t in namn2:
#     if len(t)%2==0 and t[0]=="A":
#         börja.append(t)
# print(börja)



# tal3 = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
# j1ämna=[]
# u1dda=[]
# for y in tal3:
#     if y %2==0 and y >10:
#         j1ämna.append(y)
#     elif y %2==1 and y > 10:
#         u1dda.append(y)
# print(j1ämna)
# print(u1dda)



# count=0
# tal4 = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
# for u in tal4:
#     if u %2==0 and u >10:
#         count+=1
# print(count)


# count=0
# tal5 = [3, 8, 11, 14, 17, 20, 23, 26, 29]
# for i in tal5:
#     if i %2==1 and i >10:

#        count+=1
# print(count)

# count=0
# tal6 = [5, 8, 12, 15, 18, 21, 24, 27, 30, 33]
# for o in tal6:
#     if o %3==0 and not o %2==0:
#         count+=1
# print(count)

# count=0
# tal7 = [4, 6, 9, 12, 15, 17, 20, 24, 27, 31]
# for p in tal7:
#     if p > 10 and ( p %2==0 or p %3==0):
#         count+=1
# print(count)


# count=0
# tal8 = [3, 6, 8, 11, 14, 15, 18, 21, 25, 30]
# for å in tal8:
#     if å <25 and (å %2==0 or å %3==0):
#         count+=1
# print(count)

# count=0
# tal9 = [5, 8, 12, 15, 17, 20, 24, 27, 30, 35]
# for a in tal9:
#     if a > 10 and (a < 30 and not a %3==0):
#         count+=1
# print(count)


# count=0
# tal10 = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
# for s in tal10:
#     if s >10 and (s %2==1 and not s %5==0):
#         count+=1
# print(count)


# count=0
# tal11 = [3, 6, 8, 11, 14, 15, 18, 21, 24, 27, 30]
# for d in tal11:
#     if d> 10 and ( d <30 and d%3==0 and(  not d %2==0)):
#         count+=1
# print(count)

# tal12 = [5, 10, 15, 20, 25, 30]

# f=0
# while f <len(tal12):
#     if tal12[f]>15:


#      print(tal12[f])
#     f+=1



# tal13 = [4, 9, 12, 17, 20, 25, 28, 31]

# r =0
# while r <len (tal13):
#  if tal13[r]%2==0:
  
#   print(tal13[r])
#  r+=1

# tal14 = [5, 8, 11, 14, 17, 20, 23, 26, 29]

# t=0
# while t < len(tal14):

#     if tal14[t]>15:
#         print(tal14[t])
#     t+=1


# tal15 = [3, 8, 12, 15, 19, 22, 27, 30]
# y=0
# while y < len (tal15):
#     if tal15[y] >20:
#         print(tal15[y])
#         break

#     y+=1


# tal16= [4, 9, 12, 17, 20, 25, 28, 31]
# u=0
# while u < len (tal16):
#     if tal16[u]%2==0:
#         print(tal16[u])
#         break
#     u+=1

# i=0
# count=0
# tal17 = [5, 8, 11, 14, 17, 20, 23, 26, 29]
# while i < len(tal17):
#     if tal17[i]>15:
#         count+=1
#         if count==3:
#             print(tal17[i])
#             break
#     i+=1
    


#Skriv ut det tredje udda talet i listan och
#  avsluta loopen när du hittar det
# o=0
# count=0
# tal18 = [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]

# while o < len (tal18):
#     if tal18[o]%2==1:
#         count+=1
#         if count==3:
#             print(tal18[o])
#             break
#     o+=1

#Skriv ut det andra talet som är delbart
# med 3 och avsluta loopen när du hittar det.

# p=0
# count=0
# tal19 = [6, 11, 14, 19, 22, 27, 30, 35, 38]
# while p < len (tal19):
#     if tal19[p]%3==0:
#         count+=1
#         if count==3:
#             print(tal19[p])
#             break
#     p+=1



#Skriv ut det andra talet som är jämnt och 
# avsluta loopen när  du hittar det
# å =0
# count=0
# tal20 = [5, 8, 12, 17, 21, 24, 29, 32, 36]
# while å < len(tal20):
#     if tal20[å]%2==0:
#         count+=1
#         if count==2:
#             print(tal20[å])
#             break
#     å+=1

#Skriv ut det tredje talet som är udda och 
#avsluta loopen när du hittar det

# a=0
# count=0
# tal21 = [7, 10, 13, 16, 19, 22, 25, 28, 31]
# while a < len (tal21):
#     if tal21[a]%2==1:
#         count+=1
#         if count==3:
#             print(tal21[a])
#     a+=1



#Gå igenom listan och räkna hur
# många tal som är delbara med 3.
# s= 0 
# count=0
# tal22 = [4, 9, 12, 15, 18, 21, 24, 27, 30]
# while s <len (tal22):
#     if tal22[s] %3==0:
#         count+=1
#     s+=1

# print(count)
    

#Gå igenom listan med while och räkna hur 
#många tal som är udda.
# d=0
# count=0
# tal23 = [5, 8, 11, 14, 17, 20, 23, 26, 29]
# while d < len (tal23):
#     if tal23[d]%2==1:
#         count+=1
#     d+=1
# print(count)


#Gå igenom listan med while och räkna hur 
#många tal som är större än 15.
# f=0
# count=0
# tal24= [4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
# while f < len (tal24):
#     if tal24[f]>15:
#         count+=1
#     f+=1
# print(count)

#Gå igenom listan med while.
#Lägg ihop alla tal som är jämna och skriv ut summan.
# g=0

# summa=0
# tal25= [4, 7, 12, 15, 18, 21, 25, 30]
# while g < len(tal25):
#     if tal25[g]%2==0:
    
#         summa+=tal25[g]
#     g+=1
# print(summa)
    
#Gå igenom listan med while.
#Hitta det minsta talet i listan och skriv ut det.
# tal26 = [5, 12, 7, 20, 9, 15, 3, 18]
# h = 0
# minsta = tal26[0]

# while h < len(tal26):
#     if tal26[h] < minsta:
#         minsta = tal26[h]

#     h += 1

# print(minsta)

#Gå igenom listan med while.
#Hitta det största talet och skriv ut det.

# tal27 = [8, 15, 3, 22, 11, 6, 19]
# j=0
# största=tal27[0]
# while j< len(tal27):
#     if tal27[j]>största:
#         största=tal27[j]
#     j+=1
# print(största)


#Gå igenom listan med while.
#Räkna ut summan av alla tal som är större än 10.

# k=0
# summa=0
# tal28 = [4, 7, 12, 9, 18, 21, 5, 30]
# while k < len(tal28):
#     if tal28[k]>10:
        
#         summa+=tal28[k]
#     k+=1

# print(summa)

#Gå igenom listan med while.
# #Räkna ut medelvärdet av alla tal som är större än 10.
# l=0
# count=0

# summa=0
# tal29 = [6, 11, 4, 18, 9, 25, 14, 3]
# while l < len (tal29):
#     if tal29[l]>10:
#         count+=1
#         summa+=tal29[l]
#         med=summa/count
#     l+=1
# print(med)




#Gå igenom listan med while.
#Räkna ut medelvärdet av alla jämna tal.

z=0
count=0
summua=0
tal30 = [7, 12, 5, 20, 9, 16, 3, 24]
while z < len (tal30):
    if tal30[z]%2==0:
        count+=1
        summua+=tal30[z]
        med=summua/count
    z+=1
print(med)












    





























