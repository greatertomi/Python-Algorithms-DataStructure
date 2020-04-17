# The other guy's solution
def min_platforms(arrival, departure) -> int:
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    so that no train has to wait for other(s) to leave
    """

    num_platforms = 0

    for time in range(min(arrival), max(departure) + 10, 10):
        temp_num_platforms = 0

        for i_train in range(len(arrival)):
            if (time >= arrival[i_train]) and (time < departure[i_train]):
                temp_num_platforms +=1

        if temp_num_platforms > num_platforms:
            num_platforms = temp_num_platforms

    return num_platforms

# My solution
def min_platforms2(arrival, departure):
    num_platforms = 0

    for i in range(0, len(arrival)-1):
        if arrival[i+1] < departure[i]:
            num_platforms += 1

    return num_platforms


def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]

    output = min_platforms2(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

# arrival = [900,  940, 950,  1100, 1500, 1800]
# departure = [910, 1200, 1120, 1130, 1900, 2000]
# test_case = [arrival, departure, 3]
# test_function(test_case)

# arrival = [200, 210, 300, 320, 350, 500]
# departure = [230, 340, 320, 430, 400, 520]
# test_case = [arrival, departure, 2]
# test_function(test_case)

arrivals = [200, 210, 300, 320, 350, 500]
departures = [230, 340, 320, 430, 400, 520]
print(min_platforms2(arrivals, departures))
