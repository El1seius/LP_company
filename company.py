"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
Третий уровень:
Теперь вам пригодится ещё список taxes, в котором хранится информация о налогах на сотрудников из разных департаметов.
Если department None, значит, этот налог применяется ко всем сотрудникам компании.
Иначе он применяется только к сотрудникам департмента, название которого совпадает с тем, что записано по ключу department.
К одному сотруднику может применяться несколько налогов.
13. Вывести список отделов с суммарным налогом на сотрудников этого отдела.
14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
15. Вывести список отделов с указанием месячной налоговой нагрузки – количеством денег, которые в месяц этот отдел платит налогами.
16. Вывести список отделов, отсортированный по месячной налоговой нагрузки.
17. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
18. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]


# Задание 1. Вывести названия всех отделов

name_department = [every_depart['title'] for every_depart in departments]
print(name_department)

# Задание 2. Вывести имена всех сотрудников компании.

all_name = [
            one_employer['first_name'] for every_depart in departments 
            for one_employer in every_depart['employers']
            ]
print(all_name)

# Задание 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.

show_name_with_depart = []
for every_depart in departments:
    for one_employer in every_depart['employers']:
        temp_dict = {}
        temp_dict[one_employer['first_name']] = every_depart['title']
        show_name_with_depart.append(temp_dict)

print(show_name_with_depart)

# Задание 4. Вывести имена всех сотрудников компании, которые получают больше 100к.

name_with_salary_off_100k = [
                              one_employer['first_name'] for every_depart in departments 
                              for one_employer in every_depart['employers'] 
                              if one_employer['salary_rub'] > 100000
                              ]

print(name_with_salary_off_100k)

# Задание 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).

position_with_salary_before_80k = [
                                    one_employer['position'] for every_depart in departments
                                    for one_employer in every_depart['employers']
                                    if one_employer['salary_rub'] < 80000
                                    ]

print(position_with_salary_before_80k)

# Задание 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

sum_salary_in_depart = {}
for every_depart in departments:
    sum_one_depart = sum([ one_man['salary_rub'] for one_man in every_depart['employers']], 0)
    sum_salary_in_depart[every_depart['title']] = sum_one_depart

print(sum_salary_in_depart)
