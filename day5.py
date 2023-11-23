#Strings vs lists
name='Patrick'
for i in name:
    print('>>>'+i+'<<<') #string is iterable 

newName=name[3:]
print('Nowe imie to: ', newName)

#Krotka (tuples)
trash=('Pudel', 3, 'Milk', 0.4)
print(trash[1]) # 3
print(trash[1:3]) # (3, 'Milk')
print(len(trash)) # 4
#difference between tuples and list is that tuples are unmodifiable (list is modifiable)
print(type(trash))
tuple([1,2,3,4,5]) #change list to tuple
list(('a','be','ce')) #change tuple to list
print(list('witaj')) #['w', 'i', 't', 'a', 'j']

list1=[1,2,3,4,5]
list2=list1
list2[1]='zmiana, zmiana!'
print(list2) #[1, 'zmiana, zmiana!', 3, 4, 5]
print(list1) #[1, 'zmiana, zmiana!', 3, 4, 5]
#list2=list1 only reference to list2, not all list object !
import copy
list3=copy.copy(list1) #copy list not reference
list3[0]='Tylko w liscie 3'
print(list3) #['Tylko w liscie 3', 'zmiana, zmiana!', 3, 4, 5]
print(list1) #[1, 'zmiana, zmiana!', 3, 4, 5]

#zad.1 Solve
spam=['a','b','c','d']
print(spam[int(int('3'*2)/11)]) # d

#zad.2 Create a function that takes a list as an argument and returns a
# text string with all elements separated with comma and space,
# with a conjunction before the last element there should be a conjunction 'i'.

def changeToString(wejscie):
    wynik=''
    for i in wejscie:
        if i==wejscie[-1]:
            wynik=wynik+' i '+i
        elif i==wejscie[0]:
            wynik=wynik+i
        else:
            wynik=wynik+', '+i
    
    print(wynik)
    print(type(wynik))

changeToString(['To', 'jest', 'jeden', 'ciag']) 
changeToString(['banany', 'pomarańcze', 'winogrona', 'mandarynki', 'wiśnie', 'gruszki','pistacje','trufle','rzepa']) 

#zad.3
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print(len(grid[0]))
# print(len(grid))

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], sep='', end='')
    print('\n')
