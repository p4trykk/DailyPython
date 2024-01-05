"""String - operations 
Autor: Patryk Date: 4/01/2024"""

name1='O\'Hara'
print(name1)
text1='Mr O\'Hara is a new one in the town \nHe buys apartment here.'
print(text1)
text2='Last name: O\'Hara \t First name: Francis \nBirthdate: 12\\08\\1980 \t Adress: Austin, Texas, USA'
print(text2)
text3=r'O\'Hara' #'r' before string ignore all control signs like \' \n \t or etc 
print(text3)
text4='''Mr O'Hara, 
Your cat was arrested for ducknapping little ducks last night. Please appear at the police station as a witness as soon as it possible.
Best regards,
Austin Police Chief, Max Rogan'''
print(text4)
print(name1[3]) #a
print(text2[0:17]) #Last name: O'Hara
if text3 in text4:
    print(text3+' jest w podanym łańcuchu znaków.')
else:
    print(text3+' nie ma w podanym łańcuchu znaków.')

text5='ABC'
print(text3.upper())
print(text1.lower())
print(text3.isupper())
print(text5.isupper())
print(text3.isalpha())
print(text3.istitle())
print('Jaki jest twoj ulubiony owoc?')
answer=input()
if answer.lower()=='arbuz':
    print('WoW, Mój też!!!')
else:
    print(answer+' też git, mój ulubiony to arbuz.')


while True:
    print('Podaj swój wiek')
    age=input()
    if age.isdecimal():
        break
    print('Wiek musi być podany w postaci liczby całkowitej')

shopLIst=['bread', 'milk', 'eggs', 'butter', 'tomatoes', 'yogurt', 'cheese']
print('You must buy: '+ ', '.join(shopLIst))
print(text1.split())
text6='brutal-truth-is-clearly-right-bruh'
print(text6.split('-'))
print(text6.rjust(50)) #50 is overall string length 
print(text6.ljust(50,'$'))
print(text6.center(50, '_'))

def DeluxePrintForDictionary(dic):
    for x,y in dic.items():
        print(str(x).ljust(15)+str(y).rjust(50,'.'))

itemList={'Wood': 120, 'Plastic bootle': 320, 'Glass bottle': 45, 'Polyester': 3}
DeluxePrintForDictionary(itemList)

text7='     O\'Hara has new car, wow   '
print(text7.strip())
text8='xxxxxxxKozakoooooooo'
print(text8.strip('kxo')) #remove this arguments in the edges

import pyperclip
pyperclip.copy('123456789')
print(pyperclip.paste())