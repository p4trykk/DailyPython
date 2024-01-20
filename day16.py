#file operations - poject
#Random generated 10 quiz about America's states capitals with 4 answer to choose correct one

import os
import random

usa_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

path=('C:\\Users\\ASUS\\Desktop\\DANE 03\\segregator\\programowanie\\pythonProject\\data science Python\\zadania\\quiz')

print(usa_capitals)
counter=1
for quiz in range(10):
    usa_capitals_list=list(usa_capitals.keys())
    random.shuffle(usa_capitals_list)
    print(usa_capitals_list)
    with open(os.path.join(path, f'quiz{counter}.txt'), 'w') as file:
        x=0
        for capital in usa_capitals_list:  
            if x<10:  
                answers_list=[]
                correctAnswer=usa_capitals[capital]
                usa_capitals_answer_list=list(usa_capitals.values())
                random.shuffle(usa_capitals_answer_list)
                for answer in usa_capitals_answer_list:
                    if answer!=correctAnswer:
                        answers_list.append(answer)
                answers_list=answers_list[:3]
                answers_list.append(correctAnswer)
                random.shuffle(answers_list)                    
                file.write(f'{capital}: A.{answers_list[0]} B.{answers_list[1]} C.{answers_list[2]} D.{answers_list[3]}\n')
                x+=1
        file.close()
    counter+=1