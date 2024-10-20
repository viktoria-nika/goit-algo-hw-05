def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] < target: # якщо target більше за значення посередині списку, ігноруємо ліву половину
            left = mid + 1
        elif arr[mid] > target: # # якщо target менше за значення посередині списку, ігноруємо праву половину
            right = mid - 1
            upper_bound = arr[mid]  # Потенційна верхня межа
        else:
            upper_bound = arr[mid + 1] if mid + 1 < len(arr) else None # Якщо елемент знайдено, верхня межа буде наступним елементом
            return (iterations, upper_bound)

    if left < len(arr):  # Якщо елемент не знайдено, визначаємо верхню межу
        upper_bound = arr[left]
    
    return (iterations, upper_bound)


sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5] # Наприклад
target_value = 5.0
result = binary_search(sorted_array, target_value)
print(result)  # Виведе кількість ітерацій і верхню межу