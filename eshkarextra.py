
def soldier_legs (x_index, y_index):
    x_index1 = x_index + 3
    x_index2 = x_index1
    y_index1 = y_index
    y_index2 = y_index1 + 1
    tup1 = (x_index1, y_index1)
    tup2 = (x_index2, y_index2)
    list_tuple= [tup1,tup2]
    return list_tuple

print(soldier_legs(0,0))

def soldier_body(x_index, y_index):
    list = []
    for i in range (2):
        list.append((x_index, y_index))
        counter =0
        for i in range (3):
            new_x_index = x_index + 1 + counter
            counter += 1
            list.append((new_x_index, y_index))
        y_index += 1
    return list

print(soldier_body(0,0))












#
#     tup_list= soldier_legs(0,0)
#     x1= tup_list [0][0]
#     y1 = tup_list [0] [1]
#     x2= tup_list [1][0]
#     y2 = tup_list [1][1]
#     for i in range (3):
#         num_x= x1 - 1
#         num_x2= x2 -1
#         new_tup= (num_x, x1)
#         new_tup1 = (num_x2, y1)
#         list_tup= [new_tup, new_tup1]
#
#     return list_tup
# print(soldier_body(0, 0))





    #
    # tup= []
    # x2 = x1
    # y2= y2+ 1
    # for i in range (2):
    #     x_body = x1 + 1
    #     y_body = y1
    #     x_body1 = x1 +1
    #     y_body1 = y2
    # tup1= (x1, y1)
    # tup2= ()
    #
    #
    #