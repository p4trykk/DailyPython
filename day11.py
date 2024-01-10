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

phoneNrGroupRegex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
check3=phoneNrGroupRegex.search('Mój numer telefonu to 746-904-6758 i elo')
print(check3.group(1)) #746
print(check3.group(2)) #904-6758
print(check3.group(0)) #746-904-6758 to samo co bez argumentu 
print(check3.groups()) #('746', '904-6758') wszystkie grupy w krotce
first, second = check3.groups() #rozdzielenie elementów krotki na 2 zmienne
print(first)
print(second)
phoneNrWithBracketsGroupRegex=re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
check4=phoneNrWithBracketsGroupRegex.search('Mój numer telefonu w wersji z nawiasami to (746)-904-6758 a NIE 746-904-6758 i elo elo')
print(check4.group()) #(746)-904-6758

chooseHero=re.compile(r'SpiderMan|Batman|Aquaman')
text1='Oto lista superbohaterów: Superman, Capitan America, Batman, Ironman, Spiderman i Aquaman. EL0'
check5=chooseHero.search(text1)
print(check5.group()) #Znajduje pierwsze wystąpienie z listy w chooseHero, czyli: Batman
check6=chooseHero.findall(text1)
print(check6) #findall znajduje wszystkie wystąpienia z obiektu chooseHero i zapisuje do listy
chooseHeroByMAN=re.compile(r'(Aqua|Bat|Spider|Super|Iron)man')
check7=chooseHeroByMAN.search('Lista superHERO: man, Batman, Daredevil, Flash, Capitan America, Spiderman, Thor, Ironman')
print(check7.group()) #wyszukuje tylko pierwsze wystąpienie: Batman
check8=chooseHeroByMAN.findall(text1)
print(check8) #['Super', 'Bat', 'Iron', 'Spider', 'Aqua']

WordsEnding=re.compile(r'sejm(ie|u|ów|owi)?')
check9=WordsEnding.search('W sejmie każdy poseł uczestniczy w głosowaniu.')
print(check9.group()) #sejmie
krzyzowka=re.compile(r'woda(nowa)?soda(glowa|choroba)?')
text2='fimdslkmilkgitaraadnasdawodanowasodaglowanaziretrefwodasodagg'
check10=krzyzowka.search(text2)
print(check10.group()) #pierwsze wystąpienie: wodanowasodaglowa
check11=krzyzowka.findall(text2)
print(check11) #[('nowa', 'glowa'), ('', '')]
krzyzowka2=re.compile(r'(ka)*du') # * wielokrotne powtarzanie wyrażenia w nawiasach 
text3='flugiptyuuggkakakaniszikakadusup'
check12=krzyzowka2.search(text3)
print(check12.group()) #kakadu
