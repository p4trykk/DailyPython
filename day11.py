#Regex
def isPhoneNr(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3]!='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7]!='-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print(isPhoneNr('232-444-8943')) #true
print(isPhoneNr('232-444-894')) #false
print(isPhoneNr('moshi moshi')) #false

message='Hello, I am Peter and live in Oakland. My phone numer: 556-937-3308. Bye ;D'

for x in range(len(message)):
    check=message[x:x+12]
    if isPhoneNr(check):
        print('W podanej wiadomości znaleziono numer telefonu: '+str(check))


#same situation but using regex
import re

phoneNrRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #obiekt typu Regex
check2=phoneNrRegex.search('Mój numer telefonu to 746-904-6758') #wywolanie metody tego obiektu do wyszukiwania w łańcuchu znaków zadanego wzorca
print('Znaleziono numer telefonu: '+check2.group()) #wywołanie metody group() do obiektu Match aby wyświtlić wyszukany wynik

