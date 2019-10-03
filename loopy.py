
#!/bin/python3

import math
import os
import random
import re
import sys


'''
Some notes this answer:
After a few iterations of splitting lists & trying to sort input i
settled on a pretty clean approach (in my opinion anyway):
When given some index Y for the list X, iterate in incremental
distances either side of X[Y] (starting with left) and returning
the first index which has a value lower than the one found at X[Y]

I added a simple cache to the query loop to check if we have already
figured out an answer for Y

Some pre-optimising is done by checking if
the X[Y] is lower than the minimum value in X.

I tested out a few options for sorting queries to improve cache
performance, and while there might have been improvements, it wasn't
enough to pass "case 10" so I left it out as i felt the sorting of the 
queries and then sorting the results was less clean to read.

Which brings me to "test case 10"...
So, it won't execute in time, i guess there's some really expensive/worst case
input. To get the speed required for this, I probably need to redisign some parts of 
my answer, i considered a few options:
- balanced binary tree sort of structure
- maybe something clever with hashtables
- multiprocessing (reduced cache performance though)

Ultimately, I didn't have enough time to get this properly redisigned and make it pass,
i'd love to see the input/queries for that test case if someone would be able to send them on
to me, even just to play around with on my own.
'''

def get_elems(input_data, given_index, llen, given_val):
    '''
    Takes a list of ints, an index in that list and the len of the input.
    Returns the first index left or right of the given_index with a
    value lower than the value at the given_index
    '''
    range_val = max([given_index, (llen - given_index)]) 
    # iterate over numbers from 1 -> (given_index or len - given_index)
    # explained:
    #    - we will index to i+given_index in the following loop.
    #    - range_val + given_index is the same as the len
    for i in range(1, range_val):
        # check to the left of the
        # given index.
        left_index = given_index - i
        if left_index >= 0 and input_data[left_index] < given_val:
            # this is the first element lower than
            # the given val, it is our answer. (+1 )
            return left_index + 1
        # left didn't pass, lets check right.
        right_index = given_index + i
        if right_index < llen and input_data[right_index] < given_val:
            # this is the first element lower than
            # the given val, it is our answer because
            # we have already checked the left side.
            return right_index + 1
    # no answer, return -1
    return -1


def predictAnswer(stockData, queries):
    '''
    Given 2 lists, 
    For queries[i] find closest index with a 
    value lower than the value at stockData[i]
    Returning a list of those closest indexes
    '''
    res = []
    cache= {}
    # pre-process a few vals to save some time
    # later on.
    min_in = min(stockData)
    llen = len(stockData)
    for inp in queries:
        # offset of -1 for list indexing
        inp -= 1
        if cache.get(inp):
            # check our cache to see
            # if we already got this answer
            res.append(cache[inp])
            continue
        # not in cache, need the value rn
        this_val = stockData[inp]
        if this_val <= min_in:
            # edge case catch:
            # if the val@index <= min, answer is -1
            res.append(-1)
            cache[inp] = -1
            continue
        r = get_elems(stockData, inp, llen, this_val)
        # we have an answer - update cache and append result.
        cache[inp] = r
        res.append(r)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stockData_count = int(input().strip())

    stockData = []

    for _ in range(stockData_count):
        stockData_item = int(input().strip())
        stockData.append(stockData_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = predictAnswer(stockData, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
