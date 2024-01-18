#pliki tekstowe
import os
print(os.path.join('halo', 'jajo', 'melon', 'welon')) #zwraca ściezke z dopasowanymi separatorami
myFiles=['oceny.csv','sprawozdanie.docx','prezentacja.pptx','obrazek.jpg']
for x in myFiles:
    print(os.path.join('C:\\user\\studia\\', x))

print(os.getcwd()) #zwraca katalog roboczy
os.chdir('C:\\Users\\ASUS\\Desktop') #zmiana ściezki katalogu roboczego
print(os.getcwd())

#os.makedirs('C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\zadania\\nowyFolder') # tworzy nowy folder

print(os.path.abspath('.\\DANE 01')) #zwraca pełną (bezwzględną) ścieżkę do katalogu
print(os.path.isabs('.\\DANE 01')) # zwraca wartość logiczną True, gdy ściezka jest bezwzględna (False = względna)
print(os.path.relpath('C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie')) #zwraca ciąg tekstowy reprezentujący sciezke wzgledna z podanej wzg domyslnego katalogu roboczego
print(os.path.relpath('C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie', 'C:\\')) #to samo tylko z podanym recznie katalogiem roboczym
path='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\tekst.txt'
print(os.path.dirname(path)) #zwraca wszystko przed ostatnim ukośnikiem: C:\Users\ASUS\Desktop\DANE 03\segregator
print(os.path.basename(path)) #zwraca ostani katalog: programowanie
print(os.path.split(path)) # rozbija sciezke tworząc krotke z 2 elementami: sciezki i ostatniego elementu (katalog lub plik): ('C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie', 'tekst.txt')
krotka=(os.path.dirname(path), os.path.basename(path)) #to samo co poprzedni przykład
print(krotka==os.path.split(path)) #true
print(path.split(os.path.sep)) #wyodrębnia każdy z katalogów do listy: ['C:', 'Users', 'ASUS', 'Desktop', 'DANE 03', 'segregator', 'programowanie', 'tekst.txt']

path2='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\zadania\\DailyPython'
totalsize=0
for file in os.listdir(path2):
    print('Rozmiar pliku '+file+': '+ str(os.path.getsize(os.path.join(path2, file))))
    totalsize+=os.path.getsize(os.path.join(path2, file))
print('Rozmiar całego katalogu: '+str(totalsize))

file=open(os.path.join(path2, 'day1.py'))
odczyt=file.read()
print(odczyt)

path3='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python'
file2=open(os.path.join(path3, 'panTadeusz.txt'))
odczyt2=file2.readlines() #zapis pliku tekstowego w formie listy, nowy element po nowej linii
print(odczyt2)

nowyPlik=open(os.path.join(path3, 'powitanie.txt'), 'w') #tryb zapisu
txt=nowyPlik.write('Witam')
print(txt) #5 = długość stringa
nowyPlik.close()
nowyPlik=open(os.path.join(path3, 'powitanie.txt'))
print(nowyPlik.read()) #Witam
nowyPlik=open(os.path.join(path3, 'powitanie.txt'), 'a') #tryb dołączania (nie usuwa aktualnych zmian)
txt=nowyPlik.write('Żegnam') #6 = długość dodanego stringa
print(txt)
nowyPlik.close()
nowyPlik=open(os.path.join(path3, 'powitanie.txt'))
print(nowyPlik.read()) #WitamŻegnam
nowyPlik=open(os.path.join(path3, 'powitanie.txt'), 'w') #tryb zapisu usunie poprzednie zmiany
txt=nowyPlik.write('Elo elo 3 2 0')
nowyPlik.close()
nowyPlik=open(os.path.join(path3, 'powitanie.txt'))
print(nowyPlik.read()) 