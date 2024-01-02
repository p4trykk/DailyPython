#DICTIONARIES v2
#zad.1
import pprint
recipeBook={
    'Cesar salad':{'romain lettuce': '560g', 'croutons':'200g', 'eggs': '4', 'olive': '5 tbsp', 'garlic': '3', 'parmesan cheese': '150g'},
    'Swedish meatballs':{'beef':'500g','milk':'150ml','white breadcrumbs': '75g', 'onion': '1'},
    'Pancakes':{'plain flour': '200g', 'sugar': '50g', 'baking powder': '2 tbsp', 'butter': '50g', 'egg': '2', 'milk': '250ml'}
}

for i in recipeBook.items():
    pprint.pprint(i)


#zad.2
studentsGrades={'Tomasz Cis': {'Biology': 5, 'Chemistry': 4, 'Maths': 4, 'English': 3, 'Physics': 4},
                'Maja Kaszubiak': {'Biology': 5, 'Chemistry': 5, 'Maths': 3, 'English': 5, 'Physics': 2},
                'Filip Białaka': {'Biology': 3, 'Chemistry': 3, 'Maths': 5, 'English': 2, 'Physics': 5},
                'Klaudia Wons': {'Biology': 3, 'Chemistry': 3, 'Maths': 4, 'English': 5, 'Physics': 2},
                'Florian Jajeczny': {'Biology': 4, 'Chemistry': 5, 'Maths': 5, 'English': 5, 'Physics': 5}}

mean={'Biology':0, 'Chemistry': 0, 'Maths': 0, 'English': 0, 'Physics': 0}
for x, y in studentsGrades.items():
    mean['Biology']=mean['Biology']+y.get('Biology',0)
    mean['Chemistry']=mean['Chemistry']+y.get('Chemistry',0)
    mean['Maths']=mean['Maths']+y.get('Maths',0) 
    mean['English']=mean['English']+y.get('English',0)   
    mean['Physics']=mean['Physics']+y.get('Physics',0) 

mean['Biology']=mean['Biology']/len(studentsGrades.keys())
mean['Chemistry']=mean['Chemistry']/len(studentsGrades.keys())
mean['Maths']=mean['Maths']/len(studentsGrades.keys())
mean['English']=mean['English']/len(studentsGrades.keys())
mean['Physics']=mean['Physics']/len(studentsGrades.keys())

pprint.pprint(sorted(mean.items(), reverse=True, key=lambda x:x[1]))

#zad.3
animals= {'Dog': {'Name':'Reksio', 'Age': '5', 'breed': 'Border Coolie'},
          'Cat1': {'Name':'Lewus', 'Age': '1', 'breed': 'Burmese'},
          'Cat2': {'Name':'Donek', 'Age': '3', 'breed': 'Egyptian'}}

suma=0
for x, y in animals.items():
    suma=suma+int(y['Age'])
print(suma)

animals.update({'Cat3': {'Name':'Puszek', 'Age': '8', 'breed': 'British'}})
pprint.pprint(animals)
animals.update({'Cat1': {'Name':'Klebuszek', 'Age': '1', 'breed': 'Burmese'}})
pprint.pprint(animals)
animals.pop('Cat3')
pprint.pprint(animals)
wynik=0
for x,y in animals.items():
    age=int(y['Age'])
    if wynik<age:
        wynik=age
print('Najstarsze zwierze ma tyle lat: '+str(wynik))