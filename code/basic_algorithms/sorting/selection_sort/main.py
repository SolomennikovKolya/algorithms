
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Предполагаем, что текущий элемент — минимальный
        min_index = i
        # Поиск минимального элемента в оставшейся части массива
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Обмен найденного минимального элемента с первым элементом
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Пример использования
array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print("Отсортированный массив:", sorted_array)
