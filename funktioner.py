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



def funk8(räknar8):
    list=räknar8.split()
    count=0
    for s in range(len(list)):
        if list[s][0].lower() == list[s][-1].lower():
            count+=1
    return count
print(funk8("Anna gillar banan och radar"))

































































































