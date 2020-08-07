def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    cache = {}

    for l in range(length): # basically saying over every line in df, grab the weight and find how much space is left over
        weight = weights[l]
        complement = limit - weight
        if complement in cache: # check if any other item has the same weight as 'complement'
            j = cache[complement]
            return [l, j] # when it is, return the indices for the complements
        else: # if not, cache it and move on
            cache[weight] = l

    return None
