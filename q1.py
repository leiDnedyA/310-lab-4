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

def min_coins(amount, coins):
    merge_sort(coins)
    coins = coins[::-1]
    remaining = amount
    result = 0
    while remaining != 0:
        for coin in coins:
            if coin <= remaining:
                remaining -= coin
                result += 1
                break
    return result

if __name__ == "__main__":
    amount = 63
    coins = [1, 5, 10, 25]
    print(min_coins(amount, coins))
