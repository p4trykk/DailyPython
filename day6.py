#Dictionary (słownik)

myDoggo={'name':'Ventuś', 'color':'white', 'size':'small'}
print(myDoggo['color']) # white
print('Mój piesek nazywa się '+myDoggo['name'])
roomNumbers={1:'Mr Kowalski', 2:'Mrs Walczak', 3:'Mr Nikczemny'}
print(roomNumbers[1]) # Mr Kowalski
roomNumberseverse={ 3:'Mr Nikczemny', 1:'Mr Kowalski', 2:'Mrs Walczak'}
print(roomNumbers==roomNumberseverse) #True, ponieważ elementy słownika nie są uporządkowane!
# liczy się tylko zawartość słownika a nie kolejność par klucz-wartość
roomNumbers2={2:'Mr Kowalski', 3:'Mrs Walczak', 1:'Mr Nikczemny'}
print(roomNumbers==roomNumbers2) #tutaj pary klucz-wartość są różne, dlatego False
for x in roomNumbers: 
    print(x) #domyślnie wyświetlane sa klucze!

for i in roomNumbers.values():
    print(i)

for j in roomNumbers.keys():
    print(j)

for x in roomNumbers.items():
    print(x) #domyślnie wyświetlane jako krotka

for x in roomNumbers.items():
    print(list(x)) #wyświetlane jako lista

for x, y in roomNumbers.items():
    print('Klucz: '+str(x)+', wartość: '+y)

if 'name' in myDoggo:
    print('Yes')
else: 
    print('No')

roomNumbers.setdefault(4, 'Mr Wielkomiejski')
roomNumbers.setdefault(1, 'Mr Wiejskomiejski') #nie doda bo juz klucz jest zajęty

def sprawdzKtoMieszka():
    print('Podaj numer mieszkania i sprawdze kto pod nim mieszka: ')
    numer=input()
    print('Pod numerem '+numer+' mieszka: '+roomNumbers.get(int(numer), 'nikt'))

sprawdzKtoMieszka()

slownikCech={'życzliwość':6, 'skromność': 8, 'charyzma':3}
def dodajCeche():
    print('Podaj ceche którą chcesz dodać: ')
    cecha=input()
    if cecha not in slownikCech:
        print('A teraz wartość tej cechy: ')
        wartCechy=input()
        slownikCech[cecha]=wartCechy
        print(slownikCech)
    else:
        print('Podana przez ciebie cecha już jest w słowniku! Jeśli chcesz ją zmienić wpisz TAK')
        zmiana=input()
        if zmiana=='TAK':
            print('Podaj nową zmienioną wartośc cechy: ')
            nowaWartCechy=input()
            slownikCech[cecha]=nowaWartCechy
            print(slownikCech)

dodajCeche()

#zad.1 Birthday calendar app
birthdays={}
def birthdayCalendar():
    while True:
        print('Jeżeli chcesz wyłączyć aplikacje wciśnij Q i zatwierdz jak nie to pozostaw puste pole i zatwierdz')
        nextTurn=input()
        if nextTurn=='q':
            break
        else:
            print('Podaj imię i nazwisko aby sprawdzić datę urodzin: ')
            name=input()
            if name in birthdays:
                print('Urodziny '+name+' są: '+birthdays[name])
            else:
                print('Nie ma osoby '+name+' w zestawieniu, podaj jej datę urodzin, zostanie dodana do bazy: ')
                date=input()
                birthdays[name]=date
                print('Dodano do bazy!')

birthdayCalendar()

#zad.2 letters counter in string app using dictionary
def letterCounter(doZliczenia):
    counter={}
    doZliczenia=doZliczenia.lower()
    for i in doZliczenia:
        if i==' ':
            continue
        else:
            counter.setdefault(i, 0)
            counter[i]=counter[i]+1
    counter=sorted(counter.items(), key=lambda x: x[1], reverse=True) #sortowanie od tych liter co wystapiły najcześciej
    print(dict(counter))

letterCounter('Żaba puka ci do brzucha i żuchwa')