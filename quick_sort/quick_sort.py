def quick_sort(__arr__):
    if len(__arr__) <= 1:
        return __arr__
    else:
        pivot = __arr__[0]
        less_than_pivot = [x for x in __arr__[1:] if x <= pivot]
        greater_than_pivot = [x for x in __arr__[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


arr = [5, 2, 9, 3, 7, 6, 10, 24, 35, 1000, 58, 800, 276, 1024, -2]
sorted_arr = quick_sort(arr)
print(sorted_arr)
