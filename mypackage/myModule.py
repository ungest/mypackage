def top_n(items, n):
    '''Returns the top n items in an array, in desc order.
    
    Args:
        items(array): list or array-like object
        n (int): num of items to return

    Return:
        array: top n items, in desc 
    
    Egs:
        >>> topn([8, 3, 2, 7, 4], 3)
        [8, 7, 4]
    '''

    for i in range(len(items) - 1):
        for j in range(len(items) - 1 - i):
            
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

    top_n = items[-n:]
    top_n_desc = top_n[::-1]

    return top_n_desc



