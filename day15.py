#operacje na plikach czesc 2
import shelve
import os
os.chdir('C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python')
shelfFile=shelve.open('mydata') #zapisywanie danych w programie Python (zapisywane na dysku, nie znikają po ponownym uruchomieniu)
print(type(shelfFile)) #<class 'shelve.DbfilenameShelf'>
cats=['Pookie', 'Zofie', 'Coolf', 'Zigi']
shelfFile['cats']=cats
print(shelfFile['cats']) #['Pookie', 'Zofie', 'Coolf', 'Zigi']
print(list(shelfFile.keys())) #['cats']
print(list(shelfFile.values())) #[['Pookie', 'Zofie', 'Coolf', 'Zigi']]
shelfFile.close()

import pprint

catss=[{'name': 'Zigi', 'desc':'chubby'}, {'name': 'Goofy', 'desc':'fluffy'}]
pprint.pprint(pprint.pformat(catss)) #"[{'desc': 'chubby', 'name': 'Zigi'}, {'desc': 'fluffy', 'name': 'Goofy'}]"
os.chdir('C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\zadania\\DailyPython')
saveToFile=open('tutajZapisz.py','w')
saveToFile.write('cats = '+pprint.pformat(catss)+'\n') #zapisanie listy słownikow do pliku .py (można go teraz imoprtować)
saveToFile.close()

import tutajZapisz 
print(tutajZapisz.cats[0]) #{'desc': 'chubby', 'name': 'Zigi'}
print(tutajZapisz.cats[0]['name']) #Zigi