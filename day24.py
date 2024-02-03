#Arkusze kalkulacyjne
import openpyxl, os

path='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python'
os.getcwd() #ustawienie katalogu roboczego
os.chdir(path) #zmiana katalogu roboczego
openXLSX=openpyxl.load_workbook('data.xlsx') #wczytanie skoroszytu
print(type(openXLSX)) #zwraca typ: <class 'openpyxl.workbook.workbook.Workbook'>
print(openXLSX.get_sheet_names()) #zwraca wszystkie arkusze w skoroszycie
dataSheet=openXLSX.get_sheet_by_name('Arkusz3')
print(dataSheet) #zwraca dany arkusz
print(dataSheet.title) #zwraca tytuł danego arkusza
dataSheet2=openXLSX.get_sheet_by_name('Arkusz1')
print(dataSheet2['A1'].value) #zwraca zawartość danej komórki: 2015-04-05 13:34:00
print('Komórka '+dataSheet2['B1'].coordinate+' ma wartość: '+dataSheet2['B1'].value)
print(dataSheet2.cell(row=1, column=2).value) #metoda cell również zwraca zawartość danej komórki w arkuszu: jabłka
for x in range(1,8,2):
    print(dataSheet2.cell(row=x, column=3).value) #wypisuje co drugą komórke z 3 kolumny podanego arkusza

krotka1=tuple(dataSheet2['A1':'C3'])
print(krotka1) #zwraca typy podanego zakresu komórek
#print(dataSheet2['A1':'C3'].value) #nie można wykonać bo: 'tuple' object has no attribute 'value'

for Rowcell in dataSheet2['A1':'C3']: 
    for cell in Rowcell:
        print(cell.coordinate, cell.value)
    print('--- KONIEC WIERSZA ---')

#bład zwiazany z typem generatora: "TypeError: 'generator' object is not subscriptable" - trzeba zamienić na liste i będzie GIT ;)
# print(dataSheet2.columns[1])
# for cell in dataSheet2.columns[1]:
#     print(cell.value)

