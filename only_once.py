import random

def only_once(inp):
    inp = sorted(inp)
    results = []
    dupes = []
    for i, data in enumerate(inp):
        if data in dupes:
            # already checked, skip
            continue
        try:
            if inp[i-1] == data:
                dupes.append(results)
                continue
        except IndexError:
            pass

        try:
            if inp[i+1] == data:
                dupes.append(results)
                continue
        except IndexError:
            pass

        results.append(data)

    return results


if __name__ == "__main__":
    doo = [random.randint(0, 10) for _ in range(0, 50)]
    print("Input is ", doo)
    print("output is ", only_once(doo))