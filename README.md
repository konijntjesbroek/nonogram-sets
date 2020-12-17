Nonogram sets:
Author: Arlo Gittings
In response to:

I need urgent help!!!!!!!!!!!!!!!

So, I need a function, foo, that receives a row and constraints foo(row, const), and returns the combinations according to the order in the constraints list.

The row contains the elements: 1, 0, or -1.

1 - already colored

0 - not colored

-1 - neutral (can be both colored and not colored)

Few examples of the wanted output:

    foo([1, 1, -1, 0], [3]) ---> [[1, 1, 1, 0]]  
    foo([-1, 0, 1, 0, -1, 0], [1,1]) ---> [[0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 0]]  
    foo([0, 0, -1, 1, 0] , [3]) ---> []
    This is the code I have:

    def foo(row, const, options_lst=[]):
        if len([const[j] for i in range(len(row)) if row[i:i + const[0]] == const[0]*[1] for j in range(len(const))]) >= 1:
            if row not in options_lst:
                for i in range(len(row)):
                    if row[i] == -1:
                        row[i] = 0
                options_lst.append(row)
            print(options_lst)
            return
    
        for i in range(len(row)):
            if row[i] == -1:
                row[i] = 1
                foo(row, const)
    
    foo([-1, 1, 0, 1, -1],[1,1])

    