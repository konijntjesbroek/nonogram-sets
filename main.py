'''
I need urgent help!!!!!!!!!!!!!!!

So, I need a function, foo, that receives a row and constraints foo(row, const), and returns the combinations according to the order in the constraints list.

The row contains the elements: 1, 0, or -1.

1 - already colored

0 - not colored

\-1 - neutral (can be both colored and not colored)

Few examples of the wanted output:

    foo([1, 1, -1, 0], [3]) ---> [[1, 1, 1, 0]]  
    foo([-1, 0, 1, 0, -1, 0], [1,1]) ---> [[0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 0]]  
    foo([0, 0, -1, 1, 0] , [3]) ---> []
    This is the code I have:
'''
def possible_rows(row, shape):
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

            