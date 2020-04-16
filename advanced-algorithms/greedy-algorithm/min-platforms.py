def min_platforms(arrival, departure) -> int:
    num_platforms = 0

    for time in range(min(arrival), max(departure) + 10, 10):
        temp_num_platforms = 0

        for i_train in range(len(arrival)):
            if (time >= arrival[i_train]) and (time < departure[i_train]):
                temp_num_platforms += 1
        if temp_num_platforms > num_platforms:
            num_platforms = temp_num_platforms

    return num_platforms

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
print(min_platforms(arrival, departure))
