#JSON i CSV
#a)CSV:
import csv, os
path='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python'
exampleCSV=open(os.path.join(path, 'exampleData.csv'), encoding='utf-8')
exampleReader=csv.reader(exampleCSV)
exampleDataList=list(exampleReader)
print(exampleDataList)
print(exampleDataList[0][1]) #wyswietlanie elementu listy po indeksach: jabłka
for x in exampleDataList:
    print('Wiersz #'+str(exampleReader.line_num)+ ' '+str(x)) #line_num zwraca numer wiersza 

outputFile=open(os.path.join(path, 'exampleData1.csv'), 'w', newline='', encoding='utf-8') #utworzenie nowego pliku w podanym katalogu
outputWriter=csv.writer(outputFile)
outputWriter.writerow(['2024-02-02 13:20', 'awokado', '44'])
outputFile.close()
outputFileRead=open(os.path.join(path, 'exampleData1.csv'), encoding='utf-8') 
outputReader=csv.reader(outputFileRead)
outputReaderList=list(outputReader)
print(outputReaderList)

outputFile2=open(os.path.join(path, 'exampleData1.csv'), 'w', newline='', encoding='utf-8')
outputFile2writer=csv.writer(outputFile2, delimiter='\t', lineterminator='\n\n') #rozdziela komórki tabulatorem a nie przecinkiem, a wiersze 2 nowymi wierszami
outputFile2writer.writerow(['jabłka', 'pomarańcze', 'winogrono'])
outputFile2writer.writerow(['bluszcz', 'koperek', 'stokrotka'])
outputFile2.close()
outputFileRead=open(os.path.join(path, 'exampleData1.csv'), encoding='utf-8')
outputReader=csv.reader(outputFileRead)
outputReaderList=list(outputReader)
print(outputReaderList)

#zadanie 1: usuwanie nagłówków (pierwsze wiersze) z plików CSV w danym katalogu

path2='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\headerRemove'

for file in os.listdir(path2):
    if not file.endswith('.csv'):
        continue
    else:
        csvRows=[]
        csvFile=open(os.path.join(path2, file), encoding='utf-8')
        readerfile=csv.reader(csvFile)
        for row in readerfile:
            if readerfile.line_num==1:
                continue
            csvRows.append(row)
        csvFileObj=open(os.path.join(path2, file), 'w', newline='', encoding='utf-8')
        csvWriter=csv.writer(csvFileObj)
        for row in csvRows:
            csvWriter.writerow(row)
        csvFileObj.close()
        print('Usunięto nagłówek z pliku '+str(file))

#b) JSON:
import json
stringOfJSON='{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'       
jsonDataAsPythonValue=json.loads(stringOfJSON)
print(jsonDataAsPythonValue)
pythonValue={'isCat': True, 'miceCaught': 0}
addToJSON=json.dumps(pythonValue)
print(addToJSON)

#zadanie 2: pobieranie danych o pogodzie - niestety już nie działa, bo zmieniono API docs
import requests, pprint
print('Podaj miasto, w którym chcesz sprawdzić progonozę pogody: ')
city=input()
url =f'http://api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt=3'
response=requests.get(url)
#response.raise_for_status()
weatherData=json.loads(response.text)
pprint.pprint(weatherData)
w=weatherData['list']
print(f'Aktualna pogoda w {city}: ')
print(str(w[0]['weather'][0]['main']), '-', str(w[0]['weather'][0]['description']))
print()
print('Jutro:')
print(str(w[1]['weather'][0]['main']), '-', str(w[1]['weather'][0]['description']))