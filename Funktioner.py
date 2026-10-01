# #Skapa en funktion som tar emot ett tal och returnerar talet gånger 2.
# def mult(tal):
#     return tal*2
# print(mult(5))

# #Skapa en funktion som tar emot ett tal och returnerar talet + 10.
# def mullt(tal1):
#     return tal1+10
# print(mullt(5))

#Skapa en funktion som tar emot två tal och returnerar deras summa.
# def summa(tal1, tal2):
#     return tal1 + tal2
# print(summa(4, 7))



#Skapa en funktion som tar
#emot två tal och returnerar skillnaden mellan dem.
# def summa(tal1, tal2):
#      return tal1 - tal2
# print(summa(15, 8))

#Skapa en funktion som tar emot ett tal och returnerar:
#"Jämnt" om talet är jämnt
#"Udda" om talet är udda
# def kontroll(tal):
#     if tal % 2 == 0:
#         return "Jämnt"
#     else:
#         return "Udda"
# print(kontroll( 7))



#Skapa en funktion som tar emot ett tal och returnerar:
# "Positiv" om talet är större än 0
# "Negativ" om talet är mindre än 0
# "Noll" om talet är 0
# def kontrl1(tal1):
#     if tal1 >0:
#         return "positiv"
#     elif tal1 < 0:
#         return "negativ"
#     else:
#         return "noll"
# print(kontrl1(0))

#Skapa en funktion som tar emot två tal
#och returnerar det minsta talet.
# def kontrl2(tal_1, tal_2): 
#     if tal_1 < tal_2:
#         return tal_1
#     else:
#         return tal_2
# print(kontrl2(12, 7))


#Skapa en funktion som tar emot
#tre tal och returnerar det största talet.
# def kontrl3(tal1, tal2, tal3):
#     if tal1 > tal3 and tal1> tal2:
#         return tal1
#     elif tal2 > tal1 and tal2> tal3:
#         return tal2
#     else:
#         return tal3
# print(kontrl3(4, 12, 7))






#Skapa en funktion som tar emot en lista
#med tal och returnerar summan av alla tal.

# def räkna_summa(tal):
#     summa = 0

#     for x in tal:
#         summa += x

#     return summa

# print(räkna_summa([4, 7, 3, 6]))



#Skapa en funktion som tar emot en lista med tal och
#räknar hur många tal som är större än 10.
# def count_n(tall):
#     count=0
#     for y in range(len(tall)):
#      if tall [y]>10:

#            count+=1
#     return count
# print(count_n([4, 12, 7, 18, 3, 15]))



#Skapa en funktion som tar emot
#en lista och returnerar det största talet.
# def count_n(tall):
#     störst=0
#     for y in range(len(tall)):
#      if tall [y]>störst:

#            störst=tall[y]
#     return störst
# print(count_n([7, 3, 15, 9, 12]))





#Skapa en funktion som tar emot
#en lista och returnerar det minsta talet.
# def minsta(tal33):
#     m=tal33[0]
#     for q in range(len(tal33)):
#      if tal33[q]<m:

#             m=tal33[q]
#     return m
# print(minsta([8, 4, 12, 3, 10]))
  

#Skapa en funktion som tar emot en lista och
#returnerar summan av endast de jämna talen.
# def summa_s(tal34):
#     somma=0
#     for w in range(len(tal34)):
#      if tal34[w]%2==0:
#             somma+=tal34[w]
#     return somma
# print(summa_s([3, 8, 5, 12, 7, 4]))






#Skapa en funktion som tar emot en lista och
#returnerar hur många jämna tal listan innehåller.
# def jämnna(tal35):
#     count=0
#     for e in range(len(tal35)):
#         if tal35[e]%2==0:
#             count+=1
#     return count
# print(jämnna([3, 8, 5, 12, 7, 4]))





#Skapa en funktion som tar emot en lista och returnerar
#summan av alla tal som är större än 10.
# def störrre(tal36):
#     summa=0
#     for r in range(len(tal36)):
#         if tal36[r]>10:
#             summa+=tal36[r]
#     return summa
# print(störrre([4, 12, 7, 18, 3, 15]))


#Skapa en funktion som tar emot en lista och returnerar
# det första talet som är större än 10.
# def första(tal36):
#     förstaa=tal36[0]
#     for t in range(len(tal36)):
#         if tal36[t]>10:
    
#             förstaa=tal36[t]
#             break
#     return förstaa
# print(första([4, 7, 12, 18, 3, 15]))

#Skapa en funktion som tar emot en lista och returnerar summan
#av alla udda tal som är större än 5.
# def udda_d(tal37):
#     somma=0
#     for y in range(len(tal37)):
#         if tal37[y]%2==1 and tal37[y]>5:
#             somma+=tal37[y]

#     return somma
# print(udda_d([3, 7, 12, 9, 4, 15, 8]))


#Skapa en funktion som tar emot två tal. Funktionen ska:
#returnera "Lika" om talen är lika
#annars returnera det största talet

# def kontrolll(tal38, tal39):
# def kontrolll(tal38, tal39):
#     if tal38 ==tal39:
#         return "Lika" 
#     elif tal39 > tal38:
#         return  tal39
#     else:
#         return tal38
# print(kontrolll(4, 13))

#Skapa en funktion som tar emot ett namn och ett antal år
def hälsa(namn, ålder):
    return namn, "du är", ålder 
print(hälsa("Ali", 20))























