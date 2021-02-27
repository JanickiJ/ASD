def tank(d, stations, f):
    actuald = d
    counter = 1
    stations.append(f)
    if stations[0] > d:
        return False
    else:
        actuald -= stations[0]

    for i in range(len(stations) - 1):
        print(i, actuald)
        distance = stations[i + 1] - stations[i]
        if actuald - distance >= 0:
            actuald -= distance
        else:
            actuald = d
            counter += 1
            if actuald < distance:
                return False
            else:
                actuald -= distance
    return counter

arr=[3,7,9,13,15,20]
print(tank(5,arr,22))

