from threading import Thread


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]

        thread_array_left = Thread(target=merge_sort, args=(left_array,))
        thread_array_right = Thread(target=merge_sort, args=(right_array,))
        threads = [thread_array_left, thread_array_right]

        for t in threads:
            t.start()
        for t in threads:
            t.join()

        merge(array, left_array, right_array)


def merge(array, left_array, right_array):
    i = j = k = 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1


if __name__ == '__main__':
    NUMBER_ITENS = 2 * (10**3)
    array = list(range(NUMBER_ITENS))
    array.reverse()

    merge_sort(array)
    print('Array is sorted? ', array == sorted(array))
