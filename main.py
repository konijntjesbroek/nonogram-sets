def possible_rows(row, shape):
    """
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
            InvalidRow: if row is empty of contains an invalid cell.
            InvalidShape: if shape does not exist or does not fit within row.
            No solutions: if there are no values from p_row within p_shape
    """
    if not row or [x for x in row if x > 1 or x < -1]:
        return ["Invalid Cell State"]
    else:
        p_row = build_rows(row)

    if not shape or sum(shape) + len(shape) - 1 > len(row):
        return ["Invalid Shape Passed"]
    else:
        p_shape = build_shapes(shape)

    results = [x for x in p_row if x in p_shape]

    if results:
        return results
    else: 
        return ['No valid solutions']


def build_rows(row):
    """
        build_rows:
            build a set of all possible rows given a nonogram line with some
            number of unknown values between 0 and the number of cells
        expects:
            row: (list) current cell states
        returns:
            p_row: (list) all possible cell state combinations given unknown
                   cells
        exceptions:
            None
    """

    p_row = [[],]
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
    
    return p_row

def build_shapes(shape):
    return [[1,0,0,1,0]]    


j=1

for i in possible_rows([1,-1, 0, 1,-1], [1,1]):
    print(f'{j:2d}:\t{i}')
    j+=1

            