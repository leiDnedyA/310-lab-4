def full_zero_list(n=0):
    result = []
    for _ in range(n):
        result.append(0)
    return result

def _merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    l_temp = []
    r_temp = []

    for i in range(0, n1):
        l_temp.append(arr[l + i])

    for i in range(0, n2):
        r_temp.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    while i < n1 and j < n2:
        if l_temp[i] <= r_temp[j]:
            arr[k] = l_temp[i]
            i += 1
        else:
            arr[k] = r_temp[j]
            j += 1
        k += 1

    while i < n2:
        arr[k] = l_temp[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = r_temp[j]
        j += 1
        k += 1

def _merge_sort(arr, l, r):
    if l >= r:
        return

    m = (l+r)//2

    _merge_sort(arr, l, m)
    _merge_sort(arr, m+1, r)

    _merge(arr, l, m, r)

def merge_sort(arr):
    _merge_sort(arr, 0, len(arr) - 1)

def fractional_knapsack(items, capacity):
    merge_sort(items)
    remaining_capacity = capacity
    result = 0
    while remaining_capacity != 0:
        highest_value_item = None
        for item in items:
            if item[0] <= remaining_capacity:
                if not highest_value_item or\
                        highest_value_item[1] < item[1]:
                    highest_value_item = item
        if highest_value_item:
            result += highest_value_item[1]
            remaining_capacity -= highest_value_item[0]
            print(f'adding {highest_value_item}')
        else:
            break
    return result

if __name__ == "__main__":
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50
    print("Maximum Value:", fractional_knapsack(items, capacity))
