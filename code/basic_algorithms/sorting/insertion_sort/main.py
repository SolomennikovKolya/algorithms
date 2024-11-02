
def insertion_sort(arr):
    n = len(arr)
    # Начинаем с первого элемента, предполагая, что он уже отсортирован
    for i in range(1, n):
        key = arr[i]  # текущий элемент, который нужно вставить
        j = i - 1
        # Сдвигаем элементы отсортированной части, которые больше текущего элемента
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Вставляем текущий элемент на нужное место
        arr[j + 1] = key
    return arr

# Пример использования
array = [12, 11, 13, 5, 6]
sorted_array = insertion_sort(array)
print("Отсортированный массив:", sorted_array)
