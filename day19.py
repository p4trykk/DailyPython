#raise Exception('to jest komunikat mojego wyjątku!') #trzeba zakomentować, bo inaczej nie wykonają się pozostałe instrukcje

def printowanie(sym, width, height):
    if len(sym)!=1:
        raise Exception('symbol musi być pojedynczym znakiem!')
    if width<=2:
        raise Exception('Szerokość musi mieć wartość większą od 2!')
    if height <=2:
        raise Exception('Wysokość musi mieć wartość większą od 2!')
    print(sym*width)
    for i in range(height-2):
        print(sym+(' '*(width-2))+sym)
    print(sym*width)

for s,w,h in (('*', 4,4), ('0',20,5), ('x', 1,3),('ZZ',3,3), ('@',3,3)):
    try:
        printowanie(s,w,h)
    except Exception as error:
        print('Wystąpił wyjątek: '+str(error))

#przechwytywanie błędu do pliku i dalsza realizacja kodu
import traceback, os
try:
    raise Exception('to jest komunikat błedu, HA HA')
except:
    errorFile=open(os.path.join('C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python','errorInfo.txt'), 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Informacje na temat błędu zostały zapisane w pliku errorInfo.txt')