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

p1='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python'
try:
    raise Exception('to jest komunikat błedu, HA HA')
except:
    errorFile=open(os.path.join(p1,'errorInfo.txt'), 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('Informacje na temat błędu zostały zapisane w pliku errorInfo.txt')

#assert - zastosowanie

statusOkna='otwarte'
assert statusOkna == 'otwarte', 'To okno ma być otwarte.'
statusOkna='zamknięte'
#assert statusOkna == 'otwarte', 'To okno ma być otwarte.' #asercja wychwytuje zmianę w zmiennej statusOkna i wyświetla komunikat błędu

#projekt z assert: obsługa swiateł na skrzyzowaniu
korfantego_rozdzienskiego={'ns': 'zielone', 'ew': 'czerwone'}
chorzowska_sokolska={'ns': 'czerwone', 'ew': 'zielone'}

def switchLight(skrzyzowanie):
    for key in skrzyzowanie.keys():
        if skrzyzowanie[key]=='zielone':
            skrzyzowanie[key]=='żółte'
        elif skrzyzowanie[key]=='żółte':
            skrzyzowanie[key]=='czerwone'
        elif skrzyzowanie[key]=='czerwone':
            skrzyzowanie[key]=='zielone'
    assert 'czerwone' in skrzyzowanie.values(), 'Przynajmniej jedno światło musi byc czerwone!'+str(skrzyzowanie)
switchLight(korfantego_rozdzienskiego)

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s') #DEBUG - najniższy poziom komunikatów, tylko dla sprawdzania błędów wystarczy ERROR
logging.debug('Początek programu') #każde wywołanie logging.debug wywołuje zarazem basicConfig
def factorial(n):
    logging.debug('Początek wywołania funkcji factorial(%s%%)' %(n))
    total = 1
    for i in range(n + 1): #specjalnie błąd, bo zaczynamy od zera co zawsze da zero w wyniku
        total *= i
        logging.debug('i wynosi ' + str(i) + ', wartość całkowita wynosi ' + str(total))
    logging.debug('Koniec wywołania funkcji factorial(%s%%)' %(n))
    return total
print(factorial(5))
logging.debug('Koniec programu')

#wersja poprawna:
logging.debug('Początek programu') 
def factorial(n):
    logging.debug('Początek wywołania funkcji factorial(%s%%)' %(n))
    total = 1
    for i in range(1, n + 1): #poprawione
        total *= i
        logging.debug('i wynosi ' + str(i) + ', wartość całkowita wynosi ' + str(total))
    logging.debug('Koniec wywołania funkcji factorial(%s%%)' %(n))
    return total
print(factorial(5))
logging.debug('Koniec programu')

#inne funkcje rejestrujące błędy:
logging.info('Moduł logging działa prawidłowo.')
logging.warning('Komunikat błędu przeznaczony do zarejestrowania.')
logging.error('Wystąpił błąd.')
logging.critical('Działanie programu zakończyło się awarią!')

print()
logging.disable(logging.CRITICAL)
#poniższe nie będą widoczne
logging.critical('Błąd o znaczeniu krytycznym! Błąd o znaczeniu krytycznym!')
logging.error('Błąd! Błąd!')
logging.info('Moduł logging działa prawidłowo. E L O')

#zapisywanie błędów do plików tekstowych:
filee=os.path.join(p1, 'loggingErrors.txt')
print(filee)
logging.basicConfig(filename=filee, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Moduł logging działa prawidłowo, znowu.')

