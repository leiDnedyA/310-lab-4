def min_platforms(arrival, departure):
    count, result = 0, 0
    max_departure_time = max(departure_times)
    time_counts = [0] * (max_departure_time + 2)
    for i in range(len(arrival)):
        time_counts[arrival[i]] += 1
        time_counts[departure[i] + 1] -= 1
    for i in range(max_departure_time + 2):
        count += time_counts[i]
        result = max(result, count)
    return result

if __name__ == "__main__":
    arrival_times = [900, 940, 950, 1100, 1500, 1800]
    departure_times = [910, 1200, 1120, 1130, 1900, 2000]
    print("Minimum Platforms Required:", min_platforms(arrival_times, departure_times))
