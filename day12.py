#Regex part 2

import re

phoneRegex=re.compile(r'''(
    (\d{3}|\(\d{3}\))? # opcjonalnie trzy cyfry albo trzy cyfry w nawiasach
    (\s|-|\.)? # opcjonalnie spacja, myślnik lub kropka
    \d{3} # trzy cyfry
    (\s|-|\.) # spacja, myślnik lub kropka
    \d{4} # cztery cyfry
    (\s*(ext|x|ext.)\s*\d{2,5})? # opcjonalnie rozszerzenie takie jak "ext", "x" lub "ext.", a następnie od 2 do 5 cyfr
)''', re.VERBOSE) #VERBOSE umożliwia dodawanie komentarzy w wyrażeniach regularnych

number1 = "123-456-7890"
match1 = phoneRegex.search(number1)
print(match1.group())  #  123-456-7890

number2 = "(555) 123-4567 ext. 12345"
match2 = phoneRegex.search(number2)
print(match2.group())  #  (555) 123-4567 ext. 12345

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL) #dodanie więcej opcji (flag) za pomocą potoku |
check1=someRegexValue.findall('FoO \n foO \n foooooooo')
print(check1)


#zadanie podsumowujące: program do wyszukiwania numerów telefonów komórkowych
import pyperclip

tekst=''' Dnasldn dknslad asl m smd lkmal; sml d a pjsp mdl; mlmd   +48 601 527 787 I tera zdalje jazda 

Fadqsad 

 Sa dasdasd   sdad a daddnl231 3 3 21 31 23  =1 2= 3=+  2= 3 555-234-879 fds  df sff +48 808-645-002
'''
pyperclip.copy(tekst)

def searchPhoneNumber():
    txt=pyperclip.paste()
    regex=re.compile(r'''
        (\+\d{2}|\(\+\d{2}\))? #kierunkowy z plusem na początku albo w wersji z nawiasami
        (\s)? #opcjonalnie spacja pomiędzy kierunkowym a numerem
        (\d{3}) # 3 cyfry numeru tel.
        (\s|-|\.)? # opcjonalnie spacja, myślnik lub kropka
        (\d{3}) # 3 cyfry numeru tel.
        (\s|-|\.)? # opcjonalnie spacja, myślnik lub kropka
        (\d{3}) # 3 cyfry numeru tel.
    ''', re.DOTALL | re.VERBOSE)
    checkThat=regex.findall(txt)
    if checkThat==None:
        print('Niestety nie znaleziono żadnego numeru telefonu komórkowego w podanym tekście.')
    else:
        for i in checkThat:
            print(i)

searchPhoneNumber()