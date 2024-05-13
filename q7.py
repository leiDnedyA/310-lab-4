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

def max_activities_min_duration(activities):
    durations = [end - start for start, end in activities]
    min_duration = durations[0]
    for duration in durations[1:]:
        min_duration = min(duration, min_duration)
    min_count = 0
    for duration in durations:
        if duration == min_duration:
            min_count += 1
    result = 0
    remaining_time = 8
    while remaining_time != 0:
        if min_count == 0 or remaining_time < min_duration:
            break
        min_count -= 1
        remaining_time -= min_duration
        result += 1
    return result

if __name__ == "__main__":
    activities = [(1, 3), (2, 5), (4, 6), (7, 9), (8, 10)]
    print("Maximum Number of Activities:",
    max_activities_min_duration(activities))
