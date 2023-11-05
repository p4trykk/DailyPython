#zad.1 Example usage of List
lista1=['water', 'soda', 'cola', 'milk']
print(lista1[0]) #water
print(lista1[2]) #cola
print(lista1[0:2]) #['water', 'soda']
print(lista1[:]) #['water', 'soda', 'cola', 'milk']
lista1[1]='kompot' #podmiana 'soda' na 'kompot'
lista2=[lista1, 'beer', 'tea', 'lemonade']
print(lista2[0]) #['water', 'soda', 'cola', 'milk']
print(lista2[0][2]) #cola
print(lista2[0][2:]) #['cola', 'milk']
lista3=[lista2, 2, None, True]
print(lista3[0][0][1]) #soda
print(lista3[-1]) #True
print(str(lista3[2]) + ' is used to define a null value.')
print(len(lista3)) #4 (nie uwzględnia podlist)
lista4=[1,2,3]
lista4=lista4+lista1 #Konkatenacja
print(lista4) #[1, 2, 3, 'water', 'kompot', 'cola', 'milk']
print([1, 2, 3]*3) #[1, 2, 3, 1, 2, 3, 1, 2, 3]
del lista4[2:]
print(lista4) #[1, 2]

#zad.2 Console Program using List
shopList=[]
counter=0
print('APLIKACJA KONSOLOWA - Lista Zakupów')
while True:
    print('Instrukcja obsługi: \n Wciśnij: \n 1 => dodaj produkt \n 2=> usuń produkt \n 3=> wyswietl aktualną listę zakupow \n 4=>wyjście z apki')
    odp=input()
    if int(odp)==1:
        print('Wpisz produkt, który chcesz dodać do listy zakupów: ')
        nowyProdukt=input()
        shopList.append(nowyProdukt)
        counter+=1
        print('Dzięki, produkt o nazwie: ' + nowyProdukt + ' dodano do listy!')
    elif int(odp)==2:
        print('Podaj numer indeksu produktu, ktory chcesz usunąć z listy zakupów: ')
        usunProdukt=input()
        usunProdukt=int(usunProdukt)
        usunProdukt-=1
        if usunProdukt<counter:
            del shopList[usunProdukt]
            print('Produkt o indeksie '+ str(usunProdukt+1)+' został usunięty.')
        else:
            print('Nie ma produktu o takim indeksie na liście')
    elif int(odp)==3:
        print('Aktualna lista zakupów: ')
        idx=1
        for element in shopList:
            print(str(idx) + '. ' + element, end='\n')
            idx+=1
    elif int(odp)==4:
        break