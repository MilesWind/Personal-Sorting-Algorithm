import math as m

def order_set(input_set):
    return_set = [input_set[0]]
    input_set.pop(0)
    momentum = None
    index = 0
    for x in input_set:
        index = m.floor((len(return_set)-1)/2)
        bottom = return_set[index]
        if x > bottom:
            momentum = 1
        else:
            momentum = -1
        while True:
            index += momentum
            if index == len(return_set):
                break
            if index == -1:
                index = 0
                break
            bottom = return_set[index]
            if bottom > x and momentum == 1:
                break
            if bottom < x and momentum == -1:
                index += 1
                break
        return_set.insert(index, x)
    return return_set
