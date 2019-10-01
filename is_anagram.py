


def is_anagram(words):
    '''
    takes a list of words,sorts them into a list of words grouped by anagrams
    '''
    # sort each word alphabetically, then hash in elem 0 of tuple
    sorted_k = [(hash("".join(sorted(w))), w) for w in words]
    res = sorted(sorted_k, key=lambda y: y[0])
    return [r[1] for r in res]

if __name__ == "__main__":
    words = ['foo', 'bar', 'ofo', 'rab', 'wot']
    print(is_anagram(words))
