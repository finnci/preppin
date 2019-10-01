def predict(l, i):
    if i > len(l):
        return -1
    left_list = l[:i]
    val = l[i]

    if i == 0:
        ai = 1
    else:
        ai = i + 1  # fixin awkward offset

    left_index = find_first_lowest_in_list(left_list, val, i, left=True)
    distance_left = abs(ai - left_index)

    if left_index != -1:
        max_right_i = i + distance_left + 1
    else:
        max_right_i = len(l)

    if i == 0:
        right_list = l
    else:
        right_list = l[i-1:max_right_i]

    set_left = False
    if left_index <= 0:
        set_left = True
    right_index = find_first_lowest_in_list(right_list, val, i, left_index_neg=set_left)
 
    # we have indexes, lets find the results
    if left_index == -1:
        return right_index
    elif right_index == -1:
        return left_index
    else:
        #distance_left = abs(ai - left_index)
        distance_right = abs(ai - right_index)
        if distance_left <= (distance_right):
            return left_index
        else:
            return right_index


def find_first_lowest_in_list(l, val, given_index, left=False, left_index_neg=False):
    if left:
        l.reverse()
    # set up one offset variable
    if left_index_neg and given_index == 0:
        gadder = 1
    else:
        gadder = 0
    # check all the elements we have left
    for i, v in enumerate(l):
        if v < val:
            if left:
                return given_index - i
            else:
                adder = 0
                if left_index_neg:
                    # treat as full list and increment
                    if i == 0:
                        adder += 1
                return given_index + adder + i + gadder

    return -1


if __name__ == "__main__":
    #    0, 1, 2, 3
    #    1, 2, 3, 4, 5, 6  7,  8, 9, 10
    input_data = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
    input_data = [89214, 26671, 75144, 32445, 13656, 66289, 21951, 10265, 59857, 59133, 63227, 86121, 37411, 54628, 25859, 43510, 63756, 54763, 30852, 53243, 76238, 96885, 33074, 17745, 81814, 43436, 79172, 92819, 30001, 68442, 54021, 35566, 95113, 29164, 84362, 25120, 11804, 6313, 51736, 71661, 81797, 14962, 57781, 35560, 85941, 99991, 95421, 66048, 54754, 26272, 35642, 47343, 39508, 85068, 65087, 21321, 28503, 60611, 30491, 58503, 29052, 84512, 94069, 40516, 13675, 78430, 65635, 25479, 1094, 17370, 13491, 99243, 48683, 71271, 34802, 34624, 87613, 46574, 671, 42366, 89197, 36313, 89708, 28704, 21380, 54795, 66376, 49882, 15405, 96867, 24737, 60808, 81378, 35157, 1324, 11404, 29938, 66958, 53234, 47384]
    
    queries = [80, 24, 26, 62, 46, 79, 85, 59, 52, 8, 76, 48, 72, 84, 3, 3, 30, 30, 36, 86, 96, 72, 93, 25, 28, 68, 81, 18, 78, 14, 1, 57, 90, 26, 18, 87, 56, 55, 97, 59, 62, 73, 58, 85, 8, 60, 87, 89, 89, 22]
    expected = [79 , 37 , 24 , 61 , 45 , -1 , 89 , 57 , 51 , 38 , 79 , 49 , 71 , 85 , 2 , 2 , 29 , 29 , 37 , 85 , 95 , 71 , 92 , 24 , 27 , 69 , 80 , 19 , 79 , 13 , 2 , 56 , 89 , 24 , 19 , 86 , 65 , 56 , 96 , 57 , 61 , 71 , 57 , 89 , 38 , 59 , 86 , 95 , 95 , 21]
    #expected = [2,4,-1]
    #queries = [3, 1, 8]
    res = []
    real_input = [x-1 for x in queries]
    for inp in real_input:
        res.append(predict(input_data, inp))
    print(res)
    print(expected)
    correct = 0
    for i, v in enumerate(res):
        if v == expected[i]:
            correct += 1
    print("correct ", correct)


