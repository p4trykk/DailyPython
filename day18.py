#project 1
import re, os

path='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\exercises\\day18_data'

data_pattern=re.compile(r'(0[1-9]|1[0-2])(-|\.)?(0[1-9]|[1-2][0-9]|3[01])(-|\.)?(\d{4})')

for x,y,files in os.walk(path): #zwraca kolejno listy: katalogów, podkatalogów i plików
    for file in files: #iterowanie przez pliki w docelowym katalogu
        print(file)
        file_path = os.path.join(x, file)
        with open(file_path, 'r', encoding='utf-8') as f: #dodaje uft-8 aby czytał polskie znaki
            txt=f.read() #zapisuje zawartość pliku txt do zmiennej 
            match=data_pattern.findall(txt) #wyszukiwanie regex w tekście
            for element in match:
                e=list(element) #zamieniam krotke na liste
                print(e)
                month=e[0] 
                day=e[2]
                e[0]=day #podmiana miesiecy na dni (wersja PL)
                e[2]=month #podmiana dni na miesiace (wersja PL)
                wynik=''.join(e)
                print(wynik)
                txt=txt.replace(''.join(element), wynik) #zamiana dat w wersji US na PL
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(txt)  #zapis pliku              


#project 2
print()
path2='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\zadania'
for folders, subfolders, files in os.walk(path2):
    for file in files:
        size=os.path.getsize(os.path.join(folders,file))
        if size>=2000:
            print(file+': '+str(size))

