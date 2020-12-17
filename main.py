def possible_rows(row, shape):
    """
01234567890123456789012345678901234567890123456789012345678901234567890123456789 
          1         2         3         4         5         6         7
        possible_rows:
            given a nonogram row determine if the shape requested is valid and
            return all possible combinations given the unknown cells (denoted by
            a -1) and the requested shape.
        expects:
            row: (list) current cell states
            shape: (list) widths of cells that should be in an on state, 
                   separated by at least 1 space
        returns:
            list of values from possible rows (p_row) thare are also found in
            the possible shapes (p_shape)
        exceptions:
            InvalidShape: if shape does not exist or does not fit within row.
            No solutions: if there are no values from p_row within p_shape
    """
    
    p_row = [[],]

    if not shape or sum(shape) + len(shape) - 1 > len(row):
        return ["Invalid Shape Passed"]
    else:
        p_shape = [[],]

    for i in row: # build all possible row outcomes 
        
        if i == -1: # if there is a -1, branch the possible outcomes
            temp=[]
            for j in p_row: # create a copy of all current elements
                temp.append(j.copy())

            for k in p_row: # create the postive variant for -1
                k.append(1)

            for k in temp: # create the negative variant for -1
                k.append(0)
            
            p_row.extend(temp) # add the negative variants to the positive

        else:
            for j in p_row: # cell is known add it to all possible outcomes
                j.append(i)

    results = [x for x in p_row if x in p_shape]
    if results:
        return results
    else: 
        return ['No valid solutions']
j=1

for i in possible_rows([1,-1, 0, 1,-1], [1,1]):
    print(f'{j:2d}:\t{i}')
    j+=1

            