
# Быстрая сортировка
def simple_quick_sort(array):
    n = len(array)
    if n <= 1:
        return array
    # Выбор опорного элемента (например, берём середину)
    pivot = array[n // 2]
    # Разделение массива на элементы, меньшие, равные и большие опорного
    left = [i for i in array if i < pivot]
    mid = [i for i in array if i == pivot]
    right = [i for i in array if i > pivot]
    # Рекурсивный вызов быстрой сортировки для подмассивов и объединение результатов
    return simple_quick_sort(left) + mid + simple_quick_sort(right)

# Ещё более быстрая сортировка
def quick_sort(arr, start=0, end=None):
    # start — это индекс начала подмассива, то есть самый левый элемент, с которого начинается сортировка текущего подмассива. По умолчаниню start = 0
	# end — это индекс конца подмассива, то есть самый правый элемент, до которого выполняется сортировка. По умолчаниню end = len(arr) - 1
    if end is None:
        end = len(arr) - 1
    
    while start < end:
        # Сортировка вставками для небольших подмассивов
        if end - start < 10:
            insertion_sort(arr, start, end)
            break

        pivot = median_of_three(arr, start, end)
        pivot_index = partition(arr, start, end, pivot)

        # Рекурсивно сортируем меньшую часть, а большую обрабатываем циклом
        if pivot_index - start < end - pivot_index:
            quick_sort(arr, start, pivot_index - 1)
            start = pivot_index + 1
        else:
            quick_sort(arr, pivot_index + 1, end)
            end = pivot_index - 1

    return arr

# Сортировка вставками
def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Возвращает медианный элемент среди трёх элементов массива одновременно сортируя их между собой в массиве
# То есть делает так, что arr[start] <= arr[mid] <= arr[end]
def median_of_three(arr, start, end):
    mid = (start + end) // 2
    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    if arr[mid] > arr[end]:
        arr[mid], arr[end] = arr[end], arr[mid]
    return arr[mid]

# Разбивает массив на 2 части (слева - элементы меньше опорного, справа - больше опорного) методом двух указателей
# И возвращает индекс опорного элемента
def partition(arr, start, end, pivot):
    i = start # Левый указатель
    j = end # Правый указатель
    while True:
        # Двигаем левый указатель, пока элементы левее этого указателя меньше опорного элемента
        while arr[i] < pivot:
            i += 1
        # Двигаем правый указатель, пока элементы правее этого указателя больше опорного элемента
        while arr[j] > pivot:
            j -= 1
        # Когда все элементы левее опорного элемента меньше его, а правее - болььше, возвращаем индекс опорного элемента
        if i >= j:
            return j
        # В данный момент arr[i] >= pivot and arr[j] <= pivot, поэтому если поменять i-ый и j-ый элемент местами будет: arr[i] <= pivot <= arr[j]
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

# Пример использования алгоритма
array = [3, 6, 8, 10, 1, 2, 1]
# sorted_array = simple_quick_sort(array)
sorted_array = quick_sort(array)
print("Отсортированный массив:", sorted_array)