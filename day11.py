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
krzyzowka3=re.compile(r'(ka)+du') #min. 1 wystąpienie wartości w ()
check13=krzyzowka3.search(text3)
print(check13.group()) #kakadu
text4='dadadu'
check14=krzyzowka3.search(text4)
print(check14==None) #true
haha1=re.compile(r'(Ha){3}') #dopasuj dokładnie 3 Ha, czyli: HaHaHa
text5='HaHaHaHaHaHaHa'
check15=haha1.search(text5)
print(check15.group()) #HaHaHa
haha2=re.compile(r'(Ha){3,}') #dopasuj 3 lub wiecej
check16=haha2.search(text5)
print(check16.group()) #HaHaHaHaHaHaHa - dopasowuje domyślnie najdłuższy możliwy ciąg
haha3=re.compile(r'(Ha){3,}?') #dopasowuje najkrótszy możliwy ciąg tekstowy
check17=haha3.search(text5)
print(check17.group()) #HaHaHa
haha4=re.compile(r'(Ha){,4}') #dopasuj do 4 razy zawartość () jednoznaczne do: ((Ha)|(Ha)(Ha)|(Ha)(Ha)(Ha)|(Ha)(Ha)(Ha)(Ha))
check18=haha4.search(text5)
print(check18.group()) #HaHaHaHa

#group VS findall
phoneNumRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex1.search('Tel. kom.: 415-555-9999, praca: 212-555-0000')
print(mo.group()) #group() zwraca pierwsze wystąpienie obiektu Match
mo2=phoneNumRegex1.findall('Tel. kom.: 415-555-9999, praca: 212-555-0000')
print(mo2) #findall() zwraca wszystkie możliwe wystąpienia w postaci listy: ['415-555-9999', '212-555-0000']
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo3=phoneNumRegex2.findall('Tel. kom.: 415-555-9999, praca: 212-555-0000')
print(mo3) #jezeli w wyr. reg. są grupy to findall() zwróci listę krotek: [('415', '555', '9999'), ('212', '555', '0000')]

#Signatures classes
# \d - cyfra 0-9
# \D - dowolny znak bez cyfr 0-9
# \w - dowolna litera, cyfra, znak podkreslenia
# \W - wszystko oprócz litery, cyfry lub podkreślenia
# \s - spacja, tabulator, nowa linia (białe znaki)
# \S - wszystko oprócz białych znaków

mix1=re.compile(r'\d\w\s')
check19=mix1.search('11 w2 3d gg  .c')
print(check19.group()) #11 -> pierwsze wystąpienie
check20=mix1.findall('11 w2 3d gg  .c')
print(check20) #['11 ', '3d ']
mix2=re.compile(r'\d+\s\w+') #dopasować dowolna ilość cyfr, spacja i dowolna ilość znakow
check21=mix2.findall('12 jabłek, twoja kapucynka, 1 talerzyk, g r z i b')
print(check21) #['12 jabłek', '1 talerzyk']

myOwnRegex=re.compile(r'[AaBbCc]') #własna klasa znaków
check22=myOwnRegex.findall('Wiewiórka zajada się pokarmem dla rybek. Ale SZOK!')
print(check22) #['a', 'a', 'a', 'a', 'a', 'a', 'b', 'A']
myOwnRegex2=re.compile(r'[a-z]') #dopasowanie tylko małych liter
check23=myOwnRegex2.findall('WODA TO WODA, TEGO NIE ZMIENISZ. elo')
print(check23) #['e', 'l', 'o']
myOwnRegex3=re.compile(r'[^a-z ,.]') #dopasowanie wszystkich znaków bez małych liter (a-z), spacji, przecinka i kropki
check24=myOwnRegex3.findall('jedziesz za szybko. Zwolnij!')
print(check24) #['Z', '!']
myOwnRegex4=re.compile(r'^Witam.*Żegnam$') #znajdz tekst zaczynający sie "Witam" i kończący "Żegnam" (kropka - znak wieloznaczny)
check25=myOwnRegex4.findall('Witam, miło mi Państwa widzieć. Żegnam')
print(check25) #['Witam, miło mi Państwa widzieć. Żegnam']
nameRegex=re.compile(r'Imię: (.*) Nazwisko: (.*)')
check26=nameRegex.search('Imię: Krzysztof Nazwisko: Jarzyna')
print(check26.groups(0)) #('Krzysztof', 'Jarzyna')
nongreedyRegex = re.compile(r'<.*?>') #tryb niezachłanny - dopasowanie min. wymagań 
check27 = nongreedyRegex.search('<To jest obsługa> w restauracji.>')
print(check27.group()) #<To jest obsługa>
greedyRegex = re.compile(r'<.*>') #tryb zachłanny - dopasowanie max. wymagań
check28 = greedyRegex.search('<To jest obsługa> w restauracji.>')
print(check28.group()) #<To jest obsługa> w restauracji.>
newRegexAgain=re.compile(r'.*')
check29=newRegexAgain.search('Ale jazda\ntego już nie znajdzie HE He\na tego to tym bardziej :D')
print(check29.group()) #Ale jazda  >> nie znajduje po nowej linii
newRegexAgainUpdate=re.compile(r'.*', re.DOTALL) #re.DOTALL - umozliwia pokonanie nowych linii
check30=newRegexAgainUpdate.search('Ale jazda\ntego już nie znajdzie HE He\na tego to tym bardziej :D')
print(check30.group()) #Ale jazda
#tego już nie znajdzie HE He
#a tego to tym bardziej :D
whosKnowTheSize=re.compile(r'(robocop)', re.IGNORECASE) #IGNORECASE - nie zwraca uwagi na wielkość znaków
check31=whosKnowTheSize.findall('RoBOcOp roboCOP')
print(check31) #['RoBOcOp', 'roboCOP']

regexSwap=re.compile(r'Adam \w+')
swap=regexSwap.sub('#####', 'Adam Nowak, możesz być spokojny, pozostaniesz incognito')
print(swap) # #####, możesz być spokojny, pozostaniesz incognito
regexSwap2=re.compile(r'Agencie (\w)\w*')
swap2=regexSwap2.sub('Agencie \\1###', 'Agencie Nowak, możesz być spokojny, pozostaniesz incognito')
print(swap2) # Agencie N###, możesz być spokojny, pozostaniesz incognito
