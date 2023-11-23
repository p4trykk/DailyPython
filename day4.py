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
print(lista4.index(2)) #1
lista5=['cat', 'hamster', 'dog', 'snake']
lista5.append('bear')
print(lista5) # ['cat', 'hamster', 'dog', 'snake', 'bear']
lista5.insert(0,'fish')
print(lista5) #['fish', 'cat', 'hamster', 'dog', 'snake', 'bear']
lista5.remove('snake')
print(lista5) #['fish', 'cat', 'hamster', 'dog', 'bear']
lista6=['Tomasz','Michał', 'Maja', 'Michał']
lista6.remove('Michał')
print(lista6) #['Tomasz', 'Maja', 'Michał']
lista6.sort()
print(lista6) #['Maja', 'Michał', 'Tomasz']
lista7=['a','D','A', 'c', 'AAA', 'C','aa']
lista7.sort(key=str.lower, reverse=True)
print(lista7) #['D', 'c', 'C', 'AAA', 'aa', 'a', 'A']

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

#zad3: christmas tree generator
print('Podaj długość choinki: ')
l=input()
choinka='*'
for i in range(int(l)):
    print(choinka)
    choinka=choinka+'*'

#zad4: define function that sumarize all elements in list
def sumarize(lista_do_sumowania):
    wynik=0
    for i in lista_do_sumowania:
        wynik=wynik+i
    print('Wynik to: ', wynik)

sumarize([1,2,3])
sumarize([10,5,33])

#zad5: define function to auto progessive sumarize using formula
t=[2,4,6]
t2=[1,3,6,9,123]
def progressive_sumarize(input_list):
    xn=0
    yn=1
    for i in input_list:
        xn=xn+yn*i
        print('Wynik dla '+ str(yn) + ' obrotu pętli to: '+ str(xn))
        yn+=1

progressive_sumarize(t)
progressive_sumarize(t2)

#zad6: 
def sequence_list(dist):
    for i in range(dist+1):
        for x in range(i):
            print(str(i) + ' ' + str(x))

sequence_list(5)


#zad7: clock that counting to 'end_time' with 15 minutes gap 
def clock(end_time):
    for i in range(end_time):
        minutes=0
        for j in range(4):
            if j==0:
                print(str(i)+' : '+str(minutes)+'0')
            else:
                print(str(i)+' : '+str(minutes))
            minutes+=15
clock(4)

#zad.8: Random sentense  generator with list
import random
def random_sentense():
    sentense=['zdrowia!', 'Trzymaj się!', 'Powodzenia!', 'Bedzie git', 'Na zdrowie', 'Szerokiej drogi', 'XD']
    draft=random.randint(0,len(sentense)-1)
    print('Twoja sentencja to: ', sentense[draft])

random_sentense()