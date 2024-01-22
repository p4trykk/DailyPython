import shutil, os
path1='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\zadania\\DailyPython\\day1.py'
path2='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python'
#shutil.copy(path1, path2) #kopiowanie plików
path3='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\exercises\\doKopiowania'
#shutil.move(os.path.join(path2, 'day1.py'), path3) #przenoszenie pliku do innego katalogu
#shutil.copytree(path3, os.path.join(path2, 'kopiuj')) #kopiowanie katalogów

#for file in path3:
    #os.unlink(file)

#os.rmdir(os.path.join(path2, 'kopiuj'))

import send2trash #pozwala na przenoszenie do kosza sytemowego, zamiast trwale usuwać

pliktestowy=open(os.path.join(path3, 'plikTest.txt'), 'a')
pliktestowy.write('słyszysz mnie??')
pliktestowy.close()
send2trash.send2trash(os.path.join(path3, 'plikTest.txt'))

#przechodzenie przez drzewo katalogow:
path4='C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\zadania'
for folder, subfolders, files in os.walk(path4):
    print('Katalog bieżący to: '+folder)
    for subfolder in subfolders:
        print('Podkatalog katalogu '+folder+': '+subfolder)
    for file in files:
        print('Plik katalogu '+folder+' '+file)
    print('')

