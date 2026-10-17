
#Skriv en funktion som räknar hur många
#jämna tal det finns i en lista.

# def kontroll(tal):
   
#   count = 0
#   for q in range(len(tal)):
#     if tal[q] %2==0:

#         count+=1
#   return count
# print(kontroll([4, 7, 12, 9, 16, 3])) 

#Skriv en funktion som räknar hur många tal
# som är större än 10 i listan:
# def kontroll1(tal1):
#     count = 0
#     for w in range(len(tal1)):
#         if tal1[w]>10:
#             count+=1
#     return count
# print(kontroll1([5, 12, 7, 18, 4, 21]))


#Skriv en funktion som tar emot ett namn 
#och returnerar en hälsning

# def hälsa(namn):
#     return "Hej " + namn.upper()+"!"
# print(hälsa("Ali"))

#Skriv en funktion som tar emot en text och returnerar hur många tecken den
#innehåller, utan att räkna mellanslag
# def tecken(text):
#     count =0
#     for e in range(len(text)):
#         if text[e] != "":
#             count+=1
#     return count
# print(tecken("Jag lär mig Python"))


#Skriv en funktion som tar emot ett namn.
#Om namnet innehåller fler än 5 tecken ska funktionen returnera
# def kontrll2(namn):
#     if len (namn)>5:
#         return "lång"
#     else:
#         return "kort"
# print(kontrll2("Ali"))
# print(kontrll2("Jonathan"))
# print(kontrll2("Sara"))
# print(kontrll2("Mohammed"))



#Skapa en funktion som tar emot ett namn och returnerar:

# def hälsning(namn):
#     return "Hej " + namn
# print(hälsning("Sara"))
# print(hälsning("Ali"))




#Skriv en funktion som räknar hur
#många namn som har fler än 4 tecken.
# def lista(nmann):

#     count = 0
#     for r in nmann:
#      if len(r)>4:
#         count +=1
#     return count
# print(lista(["Ali", "Jonathan", "Sara"]))


#Skriv en funktion som tar emot en lista med ord och räknar
#hur många ord som har färre än 5 tecken.
# def listaor(nammn):
#     count = 0

#     for ord in nammn:
#         if len(ord)<5:
#             count +=1
#     return count
# print(listaor(["hund", "elefant", "katt", "bil"]))








#Skriv en funktion som tar emot en lista med namn och returnerar en
#ny lista där alla namn är skrivna med stora bokstäver.

# def lista1(nnamn):
#         ny_lista = []

#         for y in range(len(nnamn)):
#                 ny_lista.append(nnamn[y].upper())

#         return ny_lista

# print(lista1(["Ali", "Sara", "Jonathan"]))


#Skriv en funktion som tar emot en lista med ord och returnerar
#en ny lista med bara ord som har fler än 3 tecken.

# def lista3(namner):
#     lista4=[]
#     for u in range(len(namner)):
#         if len(namner[u])>3:
#             lista4.append(namner[u])
#     return lista4
# print(lista3(["bil", "hund", "katt", "elefant"]))






#Skriv en funktion som tar emot en lista med namn och returnerar en
#ny lista där bara namn som börjar med bokstaven A finns kvar.
# def lis(namnA):
#     liss2=[]
#     for i in range(len(namnA)):
#         if namnA[i][0]=="A":
#             liss2.append(namnA[i])
#     return liss2
# print(lis(["Ali", "Sara", "Ahmed", "Jonathan", "Amir"]))




#Skriv en funktion som tar emot en lista med namn och returnerar en ny lista med bara 
#namnen som börjar med A, men där namnen skrivs med stora bokstäver

# def lissta11(tal1):
#     lis_ny=[]
#     for o in range(len(tal1)):
#         if tal1[o][0]=="A":
#             lis_ny.append(tal1[o].upper())
#     return lis_ny
# print(lissta11(["Ali", "Sara", "Ahmed", "Jonathan", "Amir"]))



#Skriv en funktion som tar emot en lista med ord och returnerar en
#ny lista med ord som innehåller bokstaven "a"
# def namner(lista):
#     nyy_lista=[]
#     for p in range(len(lista)):
#         if "a" in lista[p]:
#             nyy_lista.append(lista[p])
#     return nyy_lista
# print(namner(["hund", "katt", "bil", "apa", "sol"]))



#Skriv en funktion som tar emot en lista med ord och 
# returnerar en ny lista där orden som innehåller bokstaven 
# "a" skrivs med stora bokstäver. 
# Ord som inte innehåller "a" ska inte tas med.

def funkt(liss):
    bkst=[]
    for s in range(len(liss)):
        if "a" in liss[s]:
            bkst.append(liss[s].upper())
    return bkst
print(funkt(["hund", "katt", "bil", "apa", "sol"]))
































