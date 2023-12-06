# 1. Упорядочить по возрастанию элементы каждой строки матрицы размером n х m.

def sort_matrix_row(matrix):
    for row in matrix:
        row.sort() # Сортируем строку

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
    with open("ФИО_группа_vivod.txt", "w") as file:
        for row in matrix:
            # Преобразуем элементы строки в строки и объединяем их через пробел
            line = " ".join(str(elem) for elem in row)
            file.write(line + "\n") # Записываем строку в файл с символом перевода строки

matrix = load_matrix()


print("Исходная матрица:") # Выводим исходную матрицу
print_matrix(matrix)

sort_matrix_row(matrix) # Вызываем процедуру сортировку строк

print("Упорядоченная матрица:") # Выводим отсортированную матрицу
print_matrix(matrix)

save_matrix(matrix)
