def has_negatives(a):
    """
    will check if values have a negative twin.
    Basically will go through the list, find each 
    items opposite, then if it exists elsewhere, append to 
    a results list and move on, returning the list when 
    its completed.
    """
    cache = {}
    output = []
    for value in a: # for value in input
        if value != 0: # if not 0
            cache[value] = 1 # cache value is 1
            if -value in cache: # if the neg version is in the cache now
                output.append(abs(value)) # add the pos. version to output

    return output


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
