(lambda f,d:print(-f(f,d),max(f(f,d[:i]+['nj'['n'in v]]+d[i+1:])for i,v in enumerate(d)if 1-i%2)))(lambda f,d,i=0,a=0,v=[]:(-(i in v)|(i>=len(d)))*a or f(f,d,i+2*(1,(n:=int(d[i+1])))['j'in d[i]],a+n*('a'in d[i]),v+[i]),open('i').read().split())

(lambda f, d: print(  # prints (part 1, part 2)
    -f(f, d),  # negative = infinite loop, positive = normal exit
    max(  # max to get the most positive value
        f(f, d[:i] + ['nj'['n' in v]] + d[i + 1:])  # swap jmp and nop at index i
        for i, v in enumerate(d)  # iterate through all possible swaps
        if 1 - i % 2)))(  # only take indices of instructions
    lambda f, d, i=0, a=0, v=[]:  # recursive function for execution of program
    (-(i in v)  # if index visited, this is -1
     | (i >= len(d)))  # if index out of bounds, this is 1
    * a  # use previous as the sign of a
    or f(f, d,  # recursive call for next instruction
         i + 2 * (1,  # move forward 2, because instructions are of length 2
                  (n := int(d[i + 1]))  # jump to new index if 'jmp'
                  )['j' in d[i]],  # decide whether ot jump or move forward
         a + n * ('a' in d[i]),  # increment acc if 'acc'
         v + [i]),  # add current index to visited
    open('i').read().split())  # split on each instruction/argument
