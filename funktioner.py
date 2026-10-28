#Skriv en funktion som tar emot en text och räknar hur många
# ord som slutar med bokstaven a. Räkna både stort A och litet a.

# def räkna(bokstav):
#     ord=bokstav.split()
#     count=0
#     for q in range(len(ord)):
#         if ord[q][-1]=="a":
#             count+=1

#     return count
# print(räkna("Anna gillar pizza och pasta"))








#Skriv en funktion som tar emot en text 
#och räknar hur många ord som har minst 5 tecken.

# def räkna1(tecken):
#     list=tecken.split()
#     count=0
#     for w in range(len(list)):
#      if len(list[w])>=5:

#         count+=1
#     return count
# print(räkna1("Jag lär mig Python varje dag"))


#Skriv en funktion som tar emot en text och returnerar
# en ny lista med ord som har minst 4 tecken.
# def lista(ord_1):
#     ny=ord_1.split()
#     liista2=[]

#     for e in range(len(ny)):
      
#         if len(ny[e])>=4:
#             liista2.append(ny[e])
#     return liista2
# print(lista("Jag gillar att lära mig Python"))

#Skriv en funktion som tar emot en text och returnerar
# en ny lista med ord som har minst 
#fyra tecken, men där alla ord skrivs med stora bokstäver.
# def funk(text):
#     lis=text.split()
#     ny_lista=[]
#     for r in range(len(lis)):
#         if len(lis[r])>=4:
#             ny_lista.append(lis[r].upper())
#     return ny_lista
# print(funk("Jag gillar att lära mig Python"))



#Skriv en funktion som tar emot en text och räknar hur många ord som 
# börjar med bokstaven A eller a. Stora och små bokstäver ska räknas.
# def räkna7(filtera):
#     text=filtera.split()
#     count=0

    
#     for t in range(len(text)):
#         if text[t][0].lower()=="a":
#          count+=1
#     return count
# print(räkna7("Ali äter alltid apelsiner"))


#Skriv en funktion som räknar hur många 
#ord i en text som slutar med bokstaven
# def funktion(räkna):
#     bokstv=räkna.split()
#     count=0
#     for y in range(len(bokstv)):
#         if bokstv[y][-1]=="n":
#             count+=1
#     return count
# print(funktion("Ali gillar banan och melon"))


#Skriv en funktion som räknar hur många ord i en 
# text som innehåller bokstaven "a" eller "A".
# def funk1(räknar2):
#     prog=räknar2.split()
#     count=0
#     for u in range(len(prog)):
#         if "a" in prog[u].lower():
#             count+=1
#     return count
# print(funk1("Ali gillar att programmera"))



#Skriv en funktion som tar emot en text och skapar en ny
#lista med bara ord som är längre än 3 bokstäver.
# def funk2(räknar3):
 
#  skapar=räknar3.split()
#  ny_lis=[]
#  for o in range(len(skapar)):
#   if len(skapar[o])>3:
#    ny_lis.append(skapar[o])
#  return ny_lis
# print(funk2("Jag gillar att lära mig Python"))



#Skriv en funktion som skapar en ny lista med ord
#som börjar med bokstaven A eller a. Alla ord i den nya 
#listan ska dessutom skrivas med stora bokstäver.
# def funk3(bkst):
#     ord2=bkst.split()
#     lista=[]
#     for p in range(len(ord2)):
#         if ord2[p][0].lower()=="a":
#             lista.append(ord2[p].upper())
#     return lista
# print(funk3("Ali äter alltid godis och apelsiner"))

#Skriv en funktion som räknar hur många ord som har exakt 5 bokstäver.
# def funk4(räkna6):
#     orrd=räkna6.split()
#     count=0
#     for å in range(len(orrd)):
#         if len(orrd[å])==5:
#             count+=1
#     return count
# print(funk4("Ali gillar banan melon och glass"))


#Skriv en funktion som skapar en ny lista med ord som 
#innehåller minst 5 bokstäver och gör orden till små bokstäver.
# def funk5(räknar7):
#     bb=räknar7.split()
#     list_b=[]
#     for a in range(len(bb)):
#         if len(bb[a])>=5:
#             list_b.append(bb[a].lower())
#     return list_b
# print(funk5("JAG gillar PYTHON och programmering"))


#Skriv en funktion som räknar hur många ord 
#som börjar och slutar med samma bokstav.
# def funk8(räknar8):
#     list=räknar8.split()
#     count=0
#     for s in range(len(list)):
#         if list[s][0].lower() == list[s][-1].lower():
#             count+=1
#     return count
# print(funk8("Anna gillar banan och radar"))




#Skriv funktionen kontroll(text) som returnerar en 
# lista med de ord som:
#har fler än fyra bokstäver, och
#börjar med “s” (stor eller liten bokstav spelar ingen roll).

# def kontroll(text):
#     ord_o=text.split()
#     ny_lis=[]
#     for s in range(len(ord_o)):
#         if len(ord_o[s])>4 and ord_o[s][0].lower()=="s":
#          ny_lis.append(ord_o[s])

#     return ny_lis
# print(kontroll("Stefan simmar snabbt och sjunger sakta"))
# print(kontroll("Sara såg en stor snö och Sven sov"))






#Skriv räkna_s(text) som räknar hur många ord som börjar
# och slutar med samma bokstav
# (stor eller liten spelar ingen roll) och returnerar antalet.
# def räkna_s(text_1):
#     o=text_1.split()
#     count=0
#     for d in range(len(o)):
#         if o[d][0].lower()== o[d][-1].lower():
#             count+=1
#     return count
# print(räkna_s("anna bil otto hus radar"))




# Skriv en funktion längsta(text) som:
# Delar texten i ord.
# Hittar det längsta ordet.
# Returnerar ordet (text, inte längden).

# def funktion1(text11):
#      lista=text11.split()
#      längsta=lista[0]
#      for d in range(len(lista)):
#          if len(lista[d])>len(längsta):
#           längsta=(lista[d])
#      return längsta
# print(funktion1("jag älskar programmering och kaffe"))


#Skriv kortaste(text) som returnerar det kortaste ordet.
# def kortaste(text):
#      ord=text.split()
#      kort=ord[0]
#      for f in range(len(ord)):
#       if len(ord[f])< len(kort):
#          kort=(ord[f])
#      return kort
# print(kortaste("jag älskar programmering och kaffe"))
# print(kortaste("programmering och kaffe"))

#Skriv en funktion börjar_vokal(text) som räknar
# hur många ord som börjar med en vokal. Vokalerna är
# "aeiouyåäö". Stor eller liten bokstav ska inte spela roll.

# def börjar_vokal(text):
#     ny=text.split()
#     count=0
#     for g in range(len(ny)):
#         if  ny[g][0].lower() in "aeiouyåäö":
#             count+=1
#     return count
# print(börjar_vokal("apa bil ekorre hus öl"))   # ska ge 3
# print(börjar_vokal("Hus bil"))                  # ska ge 0
# print(börjar_vokal("Apa Öl"))                   # ska ge 2



# def vokaler_i_ord(text):
#     count=0
#     for h in range(len(text)):
#         if  text[h].lower() in  "aeiouyåäö":
#             count+=1
#     return count
# print(vokaler_i_ord("Hej på dig"))



# Skriv en funktion betyg(poäng) som tar emot ett tal och returnerar en text:
# 80 eller mer: "A"
# # 60 eller mer (men under 80): "B"
# # 40 eller mer (men under 60): "C"
# # annars: "F"

# def betyg(poäng):
#     if poäng >=80:
#         return "A"
#     elif poäng >=60 and poäng<80:
#         return "B"
#     elif poäng >=40 and poäng <60:
#         return "C"
#     else:
#         return "F"
# print(betyg(66))


# Skriv en funktion räkna_betyg(poänglista) som tar emot en lista med tal 
# och returnerar hur många av dem som får betyget "A" (80 eller mer).

# def räkna_betyg(poänglista):
#     count=0
#     for q in range(len(poänglista)):

#       if poänglista[q] >=80:
#         count+=1
#     return count
# print(räkna_betyg([85, 60, 92, 40, 80]))



# Nu kombinerar vi det du kan: lista, loop, if och append.
# Skriv en funktion bara_godkända(poänglista) 
# som returnerar en ny lista med de poäng som är 40 eller mer.

# def bara_godkända(poänglista):
#     ny_lista=[]
#     for w in range(len(poänglista)):
#         if poänglista[w]>=40:
#             ny_lista.append(poänglista[w])
#     return ny_lista
# print(bara_godkända([85, 30, 92, 40, 15]))



# Du ska räkna ut medelvärdet. Medelvärde är:
# lägg ihop alla tal, och dela med hur många tal det är.
# def medelvärde(poänglista):
#     summa = 0
#     for i in range(len(poänglista)):
#         summa +=(poänglista[i])

#     return summa / len(poänglista)
# print(medelvärde([80, 60, 100]))   # 80.0
# print(medelvärde([10, 20]))        # 15.0


def plus_ett(tal):
    return tal +1
print(plus_ett(4))    # 5
print(plus_ett(10))   # 11


def addera(a, b):
    return a + b
print(addera(3, 4))   # 7
print(addera(10, 5))  # 15

























      






























































































































































































