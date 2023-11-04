#zad.1 Create function that take as arg number (1-3) and print info about that. If number is out of the range in function print error.
import random
def getNr(nr):
    if nr==1:
        print('Wylosowano liczbe 1')
    elif nr==2:
        print('Wylosowano liczbe 2')
    elif nr==3:
        print('Wylosowano liczbe 3')
    else:
        print(str(nr)+' nie jest z zakresu (1-3).')

r=random.randint(1,6)
getNr(r)

#zad.2 Check what kind of type is return by function 'print'
print(type(print()))

#zad.3 Arguments in the form of keywords Keywords and print() function
print('My name is Patryk and ', end='')
print('that text is in the same line.')
print('Text','is','automatically','separated,','dont','need','take','handmade','space.',sep=' ')

#zad.4 local vs global variable
def spam():
    eggs=99
    bacon()
    print(eggs)
def bacon():
    ham=10
    eggs=0
spam()

def spam2():
    eggs=99
    eggs=bacon2()
    print(eggs)
def bacon2():
    ham=10
    eggs=0
    return eggs
spam2()

def spam3():
    print(eggs)

eggs=42
spam3()
print(eggs)

def spam4():
    global eggs
    eggs=100

eggs=55
spam4()
print(eggs)

def spam5():
    print(eggs)
    eggs=111
# spam5() # => daje błąd! próba przypisania zmiennej (uznana zostaje jako zmienna lokalna)

#zad.5 exception handling

def divide12By(number):
    try:
        return 12 / number
    except ZeroDivisionError:
        print('Nie wolno dzielić przez zero!')
    except TypeError:
        print('Musisz podac liczbę w dzieleniu!')
print(divide12By(2))
print(divide12By(0)) #generuje błąd ZeroDivisionError, ale stosując try-exception unikamy wyłączenia programu
print(divide12By('r')) #generuje błąd TypeError
print(divide12By('')) #generuje błąd TypeError

#zad.6 guess number - console app (review)
import random
print('mam na mysli pewna liczbe z zakresu od 1 do 20.')
r=random.randint(1,20)
counter=0
while True:
    print('Sprobuj odgadnac liczbe.')
    counter+=1
    try:
        guessNr=int(input())
    except:
        guessNr=''
        print('Podano niepoprawny argument wejściowy! Spróbuj ponownie.')
    if type(guessNr)!=str:
        if guessNr==r:
            print('Brawo! Udało ci się zgadnąć liczbę! Liczba prób: {counter}', counter)
            break
        elif guessNr>r:
            print('Podana liczba jest za duza')
        elif guessNr<r:
            print('Podana liczba jest za mala')
