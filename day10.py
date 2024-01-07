import pyperclip

#zad.1
pyperclip.copy('''Fauna Polski 
            Flora roślin naczyniowych
            Grzyby chronione
            Lista amonitów''')

def bulletPointAdder():
    text=pyperclip.paste()
    text=text.split('\n')
    counter=0
    for i in text:
        text[counter]=i.strip()
        print('* '+text[counter]+'\n')
        counter+=1


bulletPointAdder()

#zad.2
tableData=[['jabłka', 'pomarańcze', 'wiśnie', 'banany'],
 ['Alicja', 'Bob', 'Karol', 'Dawid'],
 ['psy', 'koty', 'łosie', 'gęsi']]

def printTable(listaCiagow):
    counter=0
    for i in range(len(tableData)+1):
        longestElement=0
        for x in tableData:
            for a in x:
                if longestElement<len(a):
                    longestElement=len(a)
            print(x[counter].rjust(longestElement),end='')
        counter+=1
        print('\n')
            

printTable(tableData)

#zad.3
passwords={'Email': 'jacekplacek333', 
           'Twitter': 'hUb4bubaGUM',
           'Facebook': 'listwaNaKolan0',
           'Discord': 'ReN0w4CJ3',
           'BocianPożyczki':'TegoHasl4NigdyNi3ZgadnieszEL0'}

def menedzerHasel(slowniczekHasel):
    print('WITAJ W MENEDZERZE HASEŁ. Zarejestruj się. \nPodaj login: ')
    login=input()
    print('A teraz hasło: ')
    haslo=input()
    print('Witaj, '+login+' >>Rejestracja przebiegła pomyślnie!')
    while True:
        print('''Wybierz z menu (wpisując numer): 
            1>> Wyszukaj danych
            2>> Dodaj nowe dane
            3>> Exit''')
        try:
            opcja=input()

            if int(opcja) in [1,2,3]:
                if int(opcja)==1:
                    print('Wybrano wyszukiwanie danych. Hasło do którego konta chcesz zobaczyć (wybierz numer):')
                    counter=1
                    for i,j in slowniczekHasel.items():
                        print(str(counter)+'>> '+i)
                        counter+=1
                    nrKonta=input()
                    try:
                        if int(nrKonta)>len(slowniczekHasel) or int(nrKonta)<=0:
                            print('Podano błędny numer! Spróbuj ponownie!')
                        else:
                            listaHasel = [{'service': key, 'password': value} for key, value in passwords.items()]
                            print('Hasło do konta '+ listaHasel[int(nrKonta)-1]['service']+ ' to: '+listaHasel[int(nrKonta)-1]['password'])
                    except ValueError as e:
                        print('Podano nieprawidłową wartość! Spróbuj ponownie')            
                if int(opcja)==2:
                    print('Wybrano dodanie nowego hasła do konta. Podaj nazwe konta: ')
                    nowaNazwaKonta=input()
                    print('A teraz hasło do tego konta: ')
                    noweHasloDoKonta=input()
                    slowniczekHasel[nowaNazwaKonta]=noweHasloDoKonta
                    print('Operacja wykonana pomyślnie!')
                if int(opcja)==3:
                    break
        except ValueError as e1:
            print('Podano nieprawidłową wartość! Spróbuj ponownie')
        else:
            print('Nie ma takiej opcji wybierz ponownie!')

menedzerHasel(passwords)