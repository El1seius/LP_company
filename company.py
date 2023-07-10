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


for every_depart in departments:
    print(every_depart['title'])

# Задание 2. Вывести имена всех сотрудников компании.


for every_depart in departments:
    for one_employer in every_depart['employers']:
        print(one_employer['first_name'])


# Задание 3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.

for every_depart in departments:
    for one_employer in every_depart['employers']:
        temp_dict = {}
        temp_dict[one_employer['first_name']] = every_depart['title']
        print(temp_dict)


# Задание 4. Вывести имена всех сотрудников компании, которые получают больше 100к.

for every_depart in departments:
    for one_employer in every_depart['employers']:
        if one_employer['salary_rub'] > 100000:
            print(one_employer['first_name'])


# Задание 5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).

for every_depart in departments:
    for one_employer in every_depart['employers']:
        if one_employer['salary_rub'] < 80000:
            print(one_employer['position'])


# Задание 6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

for every_depart in departments:
    sum_salary_in_depart = {}
    sum_one_depart = sum([ one_man['salary_rub'] for one_man in every_depart['employers']], 0)
    sum_salary_in_depart[every_depart['title']] = sum_one_depart
    print(sum_salary_in_depart)


# Второй уровень:

# Задание 7. Вывести названия отделов с указанием минимальной зарплаты в нём.

for every_depart in departments:
    name_depart = every_depart['title']
    all_salary_in_depart = [one_employer['salary_rub'] for one_employer in every_depart['employers']]
    min_salary = min(all_salary_in_depart)
    print(f'{name_depart} минимальная зарплата {min_salary}')
        

# Задание 8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.

for every_depart in departments:
    name_depart = every_depart['title']
    all_salary_in_depart = [one_employer['salary_rub'] for one_employer in every_depart['employers']]
    min_salary = min(all_salary_in_depart)
    avg_salary = round(sum(all_salary_in_depart)/len(all_salary_in_depart), 1)
    max_salary = max(all_salary_in_depart)

    print(name_depart)
    print(f'Минимальная зарплата {min_salary}')
    print(f'Средняя зарплата {avg_salary}')
    print(f'Максимальная зарплата {max_salary}')


# Задание 9. Вывести среднюю зарплату по всей компании.

all_salary_in_company = []
for every_depart in departments:
    for one_employer in every_depart["employers"]:
        all_salary_in_company.append(one_employer['salary_rub'])


avg_salary_in_company = round(sum(all_salary_in_company)/len(all_salary_in_company), 1)
print(f'Средняя зарплата в компании {avg_salary_in_company}')


# Задание 10. Вывести названия должностей, которые получают больше 90к без повторений.

position = []
for every_depart in departments:
    for one_employer in every_depart["employers"]:
        if one_employer['salary_rub'] > 90000:
            position.append(one_employer['position'])

print(f'Должности, которые получают больше 90к {set(position)}')


# Задание 11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).

female_name = {"Michelle", "Nicole", "Christina", "Caitlin"}
for every_depart in departments:
    name_depart = every_depart['title']
    salary_in_depart = []
    for one_employer in every_depart["employers"]:
        if one_employer['first_name'] in female_name:
            salary_in_depart.append(one_employer['salary_rub'])
    
    avg_salary_in_depart = round(sum(salary_in_depart)/len(salary_in_depart), 1)
    print(name_depart)
    print(f'Средняя зарплата среди девушек {avg_salary_in_depart}')


# Задание 12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
name_people = []
for every_depart in departments:
    for one_employer in every_depart["employers"]:
        if one_employer['last_name'][-1] in vowels:
            name_people.append(one_employer['first_name'])
print(set(name_people))


# Задание 13. Вывести список отделов с суммарным налогом на сотрудников этого отдела.

for every_depart in taxes:
    if every_depart['department'] is None:
        global_percent = every_depart['value_percents']

for every_depart in taxes:
    if every_depart['department'] is not None:
        sum_tax_depart = global_percent + every_depart['value_percents']
        print(f'В отделе {every_depart["department"]} суммарный налог на сотрудников {sum_tax_depart}%')


# Задание 14. Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.


def get_tax_depart(taxes):
    tax_every_depart = {}
    for every_depart in taxes: 
        if every_depart['department'] is None:
            global_percent = every_depart['value_percents']
            tax_every_depart['unified'] = global_percent

    for every_depart in taxes:
        if every_depart['department'] is not None:
            sum_tax_depart = global_percent + every_depart['value_percents']
            tax_every_depart[every_depart['department'].lower()] = sum_tax_depart
    return tax_every_depart


for one_depart in departments:
    name_department = one_depart['title'].lower()
    tax_every_depart = get_tax_depart(taxes)
    if name_department in set(tax_every_depart.keys()):
        key_depart = name_department
    else:
        key_depart = 'unified'

    print(name_department)
    for every_employer in one_depart['employers']:
        name = every_employer['first_name']
        salary_row = every_employer['salary_rub']
        salary_hand = salary_row * (100 - int(tax_every_depart.get(key_depart))) / 100
        print(f'У {name} зарплата до вычета налога {salary_row}, зарплата "на руки" {salary_hand}')


# Задание 15. Вывести список отделов с указанием месячной налоговой нагрузки – количеством денег, которые в месяц этот отдел платит налогами.

for one_depart in departments:
    name_department = one_depart['title'].lower()
    tax_every_depart = get_tax_depart(taxes)
    if name_department in set(tax_every_depart.keys()):
        key_depart = name_department
    else:
        key_depart = 'unified'

    all_salarys_in_depart = [every_employer['salary_rub'] for every_employer in one_depart['employers']]
    sum_salarys_in_depart = sum(all_salarys_in_depart)
    month_tax = sum_salarys_in_depart * int(tax_every_depart.get(key_depart))/100
    print(f'В {name_department} месячная налоговая нагрузка составляет {round((month_tax), 1)}')


# Задание 16. Вывести список отделов, отсортированный по месячной налоговой нагрузки.

depart_with_tax = {}
for one_depart in departments:
    name_department = one_depart['title'].lower()
    tax_every_depart = get_tax_depart(taxes)
    if name_department in set(tax_every_depart.keys()):
        key_depart = name_department
    else:
        key_depart = 'unified'

    all_salarys_in_depart = [every_employer['salary_rub'] for every_employer in one_depart['employers']]
    sum_salarys_in_depart = sum(all_salarys_in_depart)
    month_tax = sum_salarys_in_depart * int(tax_every_depart.get(key_depart))/100
    depart_with_tax[month_tax] = one_depart["title"]

print(sorted(depart_with_tax.items()))


# Задание 17. Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.

tax_every_depart = get_tax_depart(taxes)
for one_depart in departments:
    name_department = one_depart['title'].lower()
    if name_department not in set(tax_every_depart.keys()):
        tax_every_depart[name_department] = tax_every_depart.get('unified')

    for every_employer in one_depart["employers"]:
        tax_per_year = every_employer['salary_rub'] * 12 * tax_every_depart.get(name_department) / 100
        if tax_per_year > 100000:
            name = every_employer['first_name']
            print(name)


# Задание 18. Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов.

tax_every_depart = get_tax_depart(taxes)
tax_in_comany = {}
for one_depart in departments:
    name_department = one_depart['title'].lower()
    if name_department not in set(tax_every_depart.keys()):
        tax_every_depart[name_department] = tax_every_depart.get('unified')

    for every_employer in one_depart["employers"]:
        tax_per_year = every_employer['salary_rub'] * 12 * tax_every_depart.get(name_department) / 100
        first_name = every_employer['first_name']
        last_name = every_employer['last_name']
        tax_in_comany[tax_per_year] = f'{first_name} {last_name}'

min_tax_in_comany = sorted(tax_in_comany)[0]
name_employer_with_min_tax = tax_in_comany.get(min_tax_in_comany)
print(name_employer_with_min_tax)
