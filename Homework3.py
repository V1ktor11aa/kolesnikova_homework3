# Vika Kolesnikova
# Date: 03/03/2023
# Description: Homework 3
# Python 3.10

def pairs(numbers_string):
    if not numbers_string:
        return 0
    numbers = numbers_string.split()
    count = 0
    for number in set(numbers):
        count += numbers.count(number) * (numbers.count(number) - 1) // 2
    return count
    # Верно

def uniques(array):
    unique_elements = []
    for element in array:
        if array.count(element) == 1:
            unique_elements.append(element)
    return unique_elements
    # Верно



def ordered_list(array):  
    left = 0  
    right = len(array) - 1  
    
    while left < right:  
        if array[left] == 0 and array[right] != 0: 
            array[left], array[right] = array[right], array[left]  # Обмениваем местами 0 и ненулевой элемент
            left += 1  # Увеличиваем указатель слева
            right -= 1  # Уменьшаем указатель справа
        if array[left] != 0: 
            left += 1  # Увеличиваем указатель слева, если элемент не равен 0
        if array[right] == 0: 
            right -= 1  # Уменьшаем указатель справа, если элемент равен 0
              
    return array  # Возвращаем измененный список
    # Решение не проходит тесты



def tuple_to_list(in_tuple):
    return list(in_tuple)



def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Dictionaries
def cities(input_string): 
    lines = input_string.split('\n')  # Разбиваем входную строку на список строк
    n = int(lines[0])  # Получаем количество стран
     
    country_1 = {}  # Создаем пустой словарь для хранения соответствия городов и стран
    for i in range(1, n+1):  # Перебираем строки с информацией о странах и их городах
        country, *cities = lines[i].split()  # Разделяем строку на страну и список городов
        for city in cities: 
            country_1[city] = country  # Добавляем записи в словарь: город - страна
     
    m = int(lines[n+1])  # Получаем количество указанных городов
    output = []  # Создаем пустой список для хранения стран для указанных городов
    for j in range(n+2, n+2+m):  # Перебираем строки с указанными городами
        city = lines[j].strip()  # Получаем очередной указанный город
        output.append(country_1.get(city, "City not found"))  # Добавляем соответствующую страну в список, если город найден
     
    return '\n'.join(output)  # Возвращаем список стран в виде строки, разделяя их символом новой строки
    # Логика верна, но не проходит тесты, посмотрим на занятии

#Sets
def languages(input_string):
    lines = input_string.split('\n')
    n = int(lines[0])

    all_languages = set()
    individual_languages = set()
    first_student = True

    i = 1
    while i < len(lines):
        m = int(lines[i])
        student_languages = set(lines[i+1:i+1+m])

        if first_student:
            individual_languages = student_languages
            first_student = False
        else:
            individual_languages = individual_languages.union(student_languages)

        if not all_languages:
            all_languages = student_languages
        else:
            all_languages = all_languages.intersection(student_languages)

        i += m + 1

    return f"{len(all_languages)}\n" + "\n".join(all_languages) + f"\n{len(individual_languages)}\n" + "\n".join(individual_languages)
    # Тут решение чуть сложнее, разберем на занятии

 
def list_gen(arr1, arr2):
    # Генератор списков для комбинирования элементов из двух списков
    result = [x + y for x in arr1 for y in arr2]
    return result


def dict_gen(N):
    # Генератор словарей для создания словаря с кубами чисел от 1 до N
    result = {x: x**3 for x in range(1, N+1)}
    return result


def multiplication_table(N):
    # Генератор для формирования строк таблицы умножения от 0 до N
    for i in range(N+1):
        row = " ".join(str(i*j) for j in range(i+1))
        yield row
    # Тут есть ошибка '0\n0 1' != '0 0\n0 1', посмотрим на занятии
        
