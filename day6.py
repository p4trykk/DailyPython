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

#zad.2 letters counter in string app using dictionary + use pprint
import pprint
def letterCounter(doZliczenia):
    counter={}
    doZliczenia=doZliczenia.lower()
    for i in doZliczenia:
        if i==' ':
            continue
        else:
            counter.setdefault(i, 0)
            counter[i]=counter[i]+1
    counter=sorted(counter.items(), key=lambda x: x[1], reverse=True) #sortowanie od tych liter co wystapiły najcześciej (1=values, 0=keys in lambda func)
    pprint.pprint(dict(counter))

letterCounter('Żaba puka ci do brzucha i żuchwa')

#zad.3 tic tac toe

def gameplay():
    turn='X'
    board={'1':' ', '2':' ', '3':' ',
        '4':' ', '5':' ', '6':' ',
        '7':' ', '8':' ', '9':' ',}
    
    def showBoard(board):
        print(board['1']+' | '+board['2']+' | '+board['3'])
        print('---------')
        print(board['4']+' | '+board['5']+' | '+board['6'])
        print('---------')
        print(board['7']+' | '+board['8']+' | '+board['9'])
    showBoard(board)
    for i in range(9):    
        print(' 1 top-left \n 2 top-middle \n 3 top-right \n 4 middle-left \n 5 middle-middle \n 6 middle-right \n 7 down-left \n 8 down-middle \n 9 down-right')
        print('Postaw '+turn+' na planszy wybierając pozycję (1-9)')
        move=input()
        board[move]=turn
        showBoard(board)

        if board['1']==board['2']==board['3']==turn or board['4']==board['5']==board['6']==turn or board['7']==board['8']==board['9']==turn or board['1']==board['5']==board['9']==turn or board['3']==board['5']==board['7']==turn or board['1']==board['4']==board['7']==turn or board['2']==board['5']==board['8']==turn or board['3']==board['6']==board['9']==turn:
            print('Gracz '+turn+' wygrał grę! Gratulacje!')
            break

        if turn=='X':
            turn='O'
        else:
            turn='X'
        

gameplay()
