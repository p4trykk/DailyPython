import webbrowser
webbrowser.open('https://github.com/') #po uruchomieniu programu przekeiruje nas do strony z url

#projekt: wyszukiwanie lokalizacji w Google Maps na podstawie podanych współrzednych
# print('Podaj miejscowość, którą mam wyszukać: ')
# city=input()
# print('A teraz podaj ulicę: ')
# street=input()
# print('Jeszcze tylko numer ulicy: ')
# street_nr=input()

# webbrowser.open(f'https://www.google.pl/maps/place/{city}+{street}+{street_nr}/')

import requests, os
r=requests.get('http://www.gutenberg.org/files/27062/27062-0.txt') #plik do pobrania z adresu url 
print(type(r)) #r jako obiekt Response
if r.status_code==requests.codes.ok: #sprawdza status żądania do podanej strony www
    print('status: OK ' + str(r.status_code)) #200 - znaczy, że jest git
else:
    print('status: Error i elo ' + str(r.status_code)) #np. 404 error
print(r.text[:250]) 

p1='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python'
zapiszNaDysku=open(os.path.join(p1,'poezje_i_takie_tam.txt'), 'wb')
for x in r.iter_content(300): #ilość bajtów przekazywana w fragmencie iteracji
    zapiszNaDysku.write(x)
zapiszNaDysku.close()
#sprawdzanie błędów:
r2=requests.get('http://inventwithpython.com/strona_ktora_nie_istnieje')
try: 
    r2.raise_for_status()
except Exception as exc:
    print(f'Wystąpił błąd: %s' % (exc))