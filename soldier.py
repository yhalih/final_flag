def soldier_legs(location):
    x_index = location[0]
    y_index = location[1]
    x_index1 = x_index + 3
    x_index2 = x_index1
    y_index1 = y_index
    y_index2 = y_index1 + 1
    tup1 = (x_index1, y_index1)
    tup2 = (x_index2, y_index2)
    list_tuple = [tup1, tup2]
    return list_tuple




def soldier_body(location):
    x_index = location[0]
    y_index = location[1]
    list = []
    for i in range(2):
        list.append((x_index, y_index))
        counter = 0
        for i in range(3):
            new_x_index = x_index + 1 + counter
            counter += 1
            list.append((new_x_index, y_index))
        y_index += 1
    return list
