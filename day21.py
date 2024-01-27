import requests, bs4, os, webbrowser

res=requests.get('https://nostarch.com/')
#res.raise_for_status()
noStarchSoup=bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)
path='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\zadania\\DailyPython'
with open(os.path.join(path,'example.html'), 'w', encoding='utf-8') as file:
    file.write(str(noStarchSoup)) #zapisanie strony ze zmiennej res do pliku html na dysku

webbrowser.open(os.path.join(path,'example.html'))

readThis=open(os.path.join(path,'example.html'), 'r', encoding='utf-8')
content=readThis.read()
exampleSoup=bs4.BeautifulSoup(content, 'html.parser')
elems=exampleSoup.select('#node-745') #wyszukac ten fragment z pliku html
print('Typ: '+str(type(elems))+' długość: '+str(len(elems))+' identify in html: '+str(elems[0])+ 'text: '+str(elems[0].getText()))