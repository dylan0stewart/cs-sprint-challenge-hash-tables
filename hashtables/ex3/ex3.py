def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    length = len(arrays)

    for a in arrays: # to get access to the actual rows basically
        for num in a: # and for every number in each nested array
            if num in cache: # if the number is in the cache, add 1 to the num in the cache
                cache[num] += 1
            else:
                cache[num] = 1 # else the cache is set to 1
    return [num[0] for num in cache.items() if num[1] is length] # returning a list comp that does: for every num in the cache, check if it matches with length, and if so, return its value

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
