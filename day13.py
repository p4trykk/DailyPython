#regex exercise
#zad.1
import re

def passwordPower(haslo):
    moc=0
    if len(haslo)>=6:
        moc+=1
    if re.search(r'[A-Z]', haslo):
        moc+=1
    if re.search(r'[0-9]', haslo):
        moc+=1
    if re.search(r'[!@#$%^&*<>?:]', haslo):
        moc+=1
    return moc

print('Wpisz hasło a sprawdzimy czy jest wystarczająco dobre!')
password=input()
wynik=passwordPower(password)
print('Moc twojego hasła to: '+str(wynik)+'/4.')

#zad.2

def strip(txt):
    regex=re.compile(' ')
    swap=regex.sub('', txt)
    return swap

x=strip(' f    l   a  k i   ')
print(x)