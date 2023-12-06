# 2. Дана действительная матрица размером n х m, все элементы которой различны.
# В каждой строке выбирается элемент с наименьшим значением.
# Если число четное, то заменяется нулем, нечетное -единицей. Вывести на экран новую матрицу.


def replace_min(matrix):
    new_matrix = []

    for row in matrix:
        min_value = min(row) # Находим мин. значение в строке
        new_row = [] # Создаем новую строку
        for elem in row:
            if elem == min_value: # Если элемент равен минимальному
                elem = elem % 2 # То заменяем его по условию

            new_row.append(elem) # Добавляем элемент в новую строку
        new_matrix.append(new_row)

    return new_matrix


def print_matrix(matrix): # Процедура вывода матрицы в консоль
    for row in matrix:
        print(row)

# Функция для загрузки матрицы из файла
def load_matrix():
    matrix = []

    # Открываем файл для чтения
    with open("Анохин_УБ-31_vvod.txt", "r") as file:
        for line in file:
            # Разбиваем строку на элементы и преобразуем их в целые числа
            row = [int(elem) for elem in line.split()]
            matrix.append(row) # Добавляем строку в матрицу

    return matrix # Возвращаем матрицу

# Функция для сохранения матрицы в файл
def save_matrix(matrix):
    # Открываем файл для записи
    with open("Анохин_УБ-31_vivod.txt", "w") as file:
        for row in matrix:
            # Преобразуем элементы строки в строки и объединяем их через пробел
            line = " ".join(str(elem) for elem in row)
            file.write(line + "\n") # Записываем строку в файл с символом перевода строки


# Загружаем матрицу из файла
matrix = load_matrix()

print("Исходная матрица:") # Выводим исходную матрицу
print_matrix(matrix)

new_matrix = replace_min(matrix) # Вызов фукнции замены наим. знач

print("Измененная матрица:")
print_matrix(new_matrix)

save_matrix(new_matrix) # Сохраняем измененную матрицу в файл
