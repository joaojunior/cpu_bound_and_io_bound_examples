from merge_sort import merge_sort


def test_merge_sort(benchmark):
    NUMBER_ITENS = 2 * (10**3)
    array = list(range(NUMBER_ITENS))
    array.reverse()

    benchmark(merge_sort, array)
