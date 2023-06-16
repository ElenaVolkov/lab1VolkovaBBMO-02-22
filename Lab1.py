#Задание 1 (15)

import random

names = ['john', 'jane', 'sara', 'mark', 'emma', 'peter']
domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
locals = ['work', 'school', 'home']

def generate_email():
    name = random.choice(names)
    domain = random.choice(domains)
    local = random.choice(locals)
    return f"{name}@{domain}.{local}"

print(generate_email())

#Задание 1 (9)
def merge_arrays(arr1, arr2):
    result = []
    for item in arr1:
        if item in arr2:
            result.append(item)
    return result

arr1 = input("Введите первый массив: ").split()
arr2 = input("Введите второй массив: ").split()

merged = merge_arrays(arr1, arr2)
print("Объединенный массив: ", merged)

#Задание 2
students = [
{
"last_name": "Петров",
"first_name": "Иван",
"birthdate": (1999, 7, 15),
"subjects": [("Математика", "2022-01-10", "Иванов", 4),
("Физика\t", "2022-01-12", "Петрова", 5),
("Английский", "2022-01-15", "Сидоров", 3)],
},
{
"last_name": "Иванова",
"first_name": "Елена",
"birthdate": (2000, 3, 24),
"subjects": [("Математика", "2022-01-10", "Иванов", 5),
("Физика\t", "2022-01-12", "Петрова", 4),
("Английский", "2022-01-15", "Сидоров", 4)],
},
{
"last_name": "Сидоров",
"first_name": "Дмитрий",
"birthdate": (1998, 11, 7),
"subjects": [("Математика", "2022-01-10", "Иванов", 3),
("Физика\t", "2022-01-12", "Петрова", 4),
("Английский", "2022-01-15", "Сидоров", 5)],
},
]

search_last_name = input("Введите фамилию студента: ")
search_first_name = input("Введите имя студента: ")

for student in students:
  if student["last_name"] == search_last_name and student["first_name"] == search_first_name: 
    # Если студент найден - выводим таблицу его предметов и оценок
    print(f"Предмет\t\tОценка")
    for subject in student["subjects"]:
      for student in students:
        print(f"{subject[0]}\t{subject[3]}")
        break
