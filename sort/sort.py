from random import randrange

def selection_sort(data: list):
    result = []
    source = data[:]
    ln = len(source)

    for _ in range(ln):
        a = source[0]

        for value in source[1:]:
            if a > value:
                a = value

        result.append(a)
        source.remove(a)

    return result

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        less = [val for val in array if val <= pivot]
        greater = [val for val in array if val > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)

def bubble_sort(array):
    if len(array) < 2:
        return array

    result = array[:]

    for i in range(len(result)):
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result

def merge_sort(array):
    if len(array) < 2:
        return array

    half = len(array) // 2

    first_half = array[0:half]
    second_half = array[half:]

    first_half = merge_sort(first_half)
    second_half = merge_sort(second_half)

    i = j = 0

    result = []

    while True:
        if i < len(first_half) and j < len(second_half):
            if first_half[i] < second_half[j]:
                result.append(first_half[i])
                i += 1
            else:
                result.append(second_half[j])
                j += 1
        elif i < len(first_half):
            result.append(first_half[i])
            i += 1
        elif j < len(second_half):
            result.append(second_half[j])
            j += 1
        else:
            break

    return result

def count_sort(array):
    '''
    O(n + maxx)
    constraint: 0 <= elem <= maxx
    '''
    arr = array[:]

    maxx = max(arr) + 1
    aux = [0] * maxx

    for elem in arr:
        aux[elem] += 1

    res = []

    for i in range(maxx):
        for _ in range(aux[i]):
            res.append(i)

    return res


def radex_sort(array):
    '''
    O((n + b) * Log b (maxx))
    '''
    arr = array[:]
    mx = max(arr)
    n = len(arr)
    last = 1
    curr = 10

    while mx:
        ind = [[], [], [], [], [], [], [], [], [], []]

        for i in range(n):
            ind[(arr[i] % curr) // last].append(i)

        new_arr = []
        for row in ind:
            for i in row:
                new_arr.append(arr[i])
                # print(arr[i], end=' ')
        # print('')

    return arr

if __name__ == '__main__':
    print(merge_sort([1,7,3,5,1,9]))
    print(merge_sort([1,2,3,4,5,9]))
    print(merge_sort([9,2,8,1,7,6]))