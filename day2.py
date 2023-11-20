#zad1: proste zadanko z pętlą while
name=''
while name != 'my name':
    print('Type my name: ')
    name=input()
print('Thx')

#zad2: weryfikacja imienia i wieku z petlami
while True:
    print('Whats your name? ')
    name2=input()
    if name2 == 'Kuba':
        print('How old are you?')
        age=input()
        if int(age) >=18:
            print('Everythink is ok! ' + name2 + ', welcome in my server :D')
            break
        else:
            print('You are too young... sorry')
    else:
        print('We dont have you ' + name2 + ' on the list, try again.')

#zad3: zabawa z petlą for
for i in range(10,20):
    if i%2==0:
        print(str(i)+' jest parzyste')
    else: 
        print(str(i)+' jest nieparzyste')

#zad3b: to samo tylko malejąco
for i in range(19,9,-1):
    if i%2==0:
        print(str(i)+' jest parzyste.')
    else: 
        print(str(i)+' jest nieparzyste.')

#zad4: to samo co w zad3 tylko z while
a=10
while a<20:
    if a%2==0:
        print(str(a)+' jest parzyste')
    else: 
        print(str(a)+' jest nieparzyste')
    a+=1

#zad5: wylosowanie randomowych 10 cyfr z petla for (przedzial 0-100)
import random #aby wykorzystać gotową funkcje random trzeba ja zaimportować
for i in range(10):
    print(random.randint(0,100))

#zad6: utworz program, który będzie losował liczby z przedziału 0-10, gdy pojawi sie 7 
#program ma sie wyłączyć (import sys) + jakis komunikat
import sys
while True:
    r=random.randint(0,10)
    print(str(r))
    if r==7:
        print('This is the end.')
        sys.exit()



    