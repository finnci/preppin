import dis



def get_elems(input_data, given_index, llen):
    given_val = input_data[given_index]
    range_val = max([given_index, (llen - given_index)])
    for i in range(1, range_val):
        if given_index - i >= 0:
            left_elem = input_data[given_index - i]
            if left_elem < given_val:
                return given_index - i + 1
        if given_index + i < llen:
            right_elem = input_data[given_index + i]
            if right_elem < given_val:
                return given_index + i + 1
    return -1


#def predictAnswer(stockData, queries):
#    real_input = [(stockData, x-1) for x in queries]   
#    res = []
#    with Pool(multiprocessing.cpu_count()) as p:
#        res.append(p.starmap(predict, real_input))
#    return res[0]

def predictAnswer(stockData, queries):
    res = []
    cache = {}
    #min_in = min(stockData)
    llen = len(stockData)
    for inp in queries:
        inp -= 1
        # try
        #     res.append(cache[inp])
        #     continue
        # except:
        #     # just pass
        #     pass
        if cache.get(inp):
            res.append(cache[inp])
            continue
        #if stockData[inp] == min_in:
        #    res.append(-1)
        #    cache[inp] = -1
        #    continue
        r = get_elems(stockData, inp, llen)
        cache[inp] = r
        res.append(r)
    return res


if __name__ == "__main__":
    #    0, 1, 2, 3
    #    1, 2, 3, 4, 5, 6  7,  8, 9, 10
    #input_data = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
    input_data = [89214, 26671, 75144, 32445, 13656, 66289, 21951, 10265, 59857, 59133, 63227, 86121, 37411, 54628, 25859, 43510, 63756, 54763, 30852, 53243, 76238, 96885, 33074, 17745, 81814, 43436, 79172, 92819, 30001, 68442, 54021, 35566, 95113, 29164, 84362, 25120, 11804, 6313, 51736, 71661, 81797, 14962, 57781, 35560, 85941, 99991, 95421, 66048, 54754, 26272, 35642, 47343, 39508, 85068, 65087, 21321, 28503, 60611, 30491, 58503, 29052, 84512, 94069, 40516, 13675, 78430, 65635, 25479, 1094, 17370, 13491, 99243, 48683, 71271, 34802, 34624, 87613, 46574, 671, 42366, 89197, 36313, 89708, 28704, 21380, 54795, 66376, 49882, 15405, 96867, 24737, 60808, 81378, 35157, 1324, 11404, 29938, 66958, 53234, 47384]
    
    queries = [80, 24, 26, 62, 46, 79, 85, 59, 52, 8, 76, 48, 72, 84, 3, 3, 30, 30, 36, 86, 96, 72, 93, 25, 28, 68, 81, 18, 78, 14, 1, 57, 90, 26, 18, 87, 56, 55, 97, 59, 62, 73, 58, 85, 8, 60, 87, 89, 89, 22]
    expected = [79 , 37 , 24 , 61 , 45 , -1 , 89 , 57 , 51 , 38 , 79 , 49 , 71 , 85 , 2 , 2 , 29 , 29 , 37 , 85 , 95 , 71 , 92 , 24 , 27 , 69 , 80 , 19 , 79 , 13 , 2 , 56 , 89 , 24 , 19 , 86 , 65 , 56 , 96 , 57 , 61 , 71 , 57 , 89 , 38 , 59 , 86 , 95 , 95 , 21]
    #expected = [2,4,-1]
    #queries = [3, 1, 8]
    res = predictAnswer(input_data, queries)
    print(dis.dis(predictAnswer))
    print(expected)
    print(res)


