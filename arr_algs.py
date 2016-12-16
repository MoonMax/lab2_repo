def min_in_arr(arr):
    r = arr[0]
    for item in arr:
        if item < r:
            r = item
    return r

def avg(arr):
    return sum(arr) / len(arr)

list1 = [10, 2, 4, 1, 3, 40]
print ('Минимум в массиве 1: ', min_in_arr(list1))
print ('Среднее в массиве 1: ', avg(list1))

print ('\n')

list2 = [150, 10, 15, 25]
print ('Минимум в массиве 2: ', min_in_arr(list2))
print ('Среднее в массиве 2: ', avg(list2))