import pyperclip

pyperclip.copy('''Fauna Polski 
            Flora roślin naczyniowych
            Grzyby chronione
            Lista amonitów''')

def bulletPointAdder():
    text=pyperclip.paste()
    text=text.split('\n')
    counter=0
    for i in text:
        text[counter]=i.strip()
        print('* '+text[counter]+'\n')
        counter+=1


bulletPointAdder()