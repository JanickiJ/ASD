def max_guests(exits, enters):
    enters.sort()
    exits.sort()
    enter = 0
    exit = 0
    counter = 0
    max_visitors = 0
    while enter < len(enters):
        if enters[enter] < exits[exit]:
            counter += 1
            enter+=1
        elif enters[enter] > exits[exit]:
            counter -= 1
            exit +=1
        else:
            enter += 1
            exit += 1
        if counter > max_visitors:
            max_visitors = counter
    return max_visitors

enters=[1,2,3,5,9,10,11,12]
exits=[4,6,7,8,14,15,17,20,20,20,13]
print(max_guests(exits,enters))