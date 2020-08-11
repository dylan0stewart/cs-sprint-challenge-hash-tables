# Your code here



def finder(files, queries):
    """
    Finder will isolate the filename from the filepath, then 
    check to see if there are matches in the query. If there are, 
    they will be added to a list of results and returned
    """
    cache = {}
    listed_results = [] # empty list for later
    for path in files: # for each filepath given, split on the second to last / to get filename
        file_item = path.split('/')[-1]
 
        if file_item in cache: # if filename is in cache
            cache[file_item].append(path) # append that path to the cache
        else: 
            cache[file_item] = [path]

    for query in queries: # for each query
        if query in cache: # if the query(aka filename) is in the cache(from the above if statement), append query to the results list
            listed_results.append(cache[query]) 
    results = [] # instantiate results

    for sublist in listed_results: # for each list in the list of results
        for item in sublist: # check through those lists, appending each item to the results list
            results.append(item)

    return results # return the results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
