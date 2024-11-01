
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Флаг, чтобы отследить, происходил ли обмен в текущем проходе
        swapped = False
        # Проход по массиву до последнего неотсортированного элемента
        for j in range(n - 1 - i):
            # Сравнение соседних элементов
            if arr[j] > arr[j + 1]:
                # Если порядок нарушен, меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не было обменов, то массив уже отсортирован
        if not swapped:
            break
    return arr

# Пример использования
array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
print("Отсортированный массив:", sorted_array)
