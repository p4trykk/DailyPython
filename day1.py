print('Hallo, its me ;D') #przywitanie
print('Whats your name bro?') #zapytanie o imię
name=input() #komenda wpisania imienia w konsoli
print('Whats up, ' + name) #wyświetlenie reakcji na podane imię
print('Length of your name is: ' + str(len(name))) #podanie długości imienia
print('How old are u?') #zapytanie o wiek
age=input() #komenda wpisania wieku w konsoli
print('Nice, ' + age + ' is very good age, bro. Next year you will have a ' + str(int(age)+1) + ' yo.') #reakcja na wiek (wypisanie go w konsoli) + obliczenie wieku na przyszły rok

#podany przykład opisuje zasade przypisywania: po uruchomieniu kodu zmienna 'a' bedzie dalej 20.
a=20
a+1
print(a)
#wykorzystanie funkcji round do zaokrąglania
b=21.523424124
b=round(b)
print(b)
c=21.32523423
c=round(c,2) #dwa msc po przecinku
print(c)