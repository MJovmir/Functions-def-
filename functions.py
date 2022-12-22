####  DRAW Christmas Tree

#               p  h  s
#   + + *       2  1  1
#   + * * *     1  2  3 
#   * * * * *   0  3  5 
# * * * * * * *    4  7


def triangle(h,o,sk):
    s=1
    p=h-1
     
    for r in range(h):
       if r == 1:
            print("", end="")
       else: 
        print( "  "* o + "  " * p + "* " * s)
        s += 2
        p -= 1
        
        
#######################
triangle(3,4,0)
triangle(5,2,0)
triangle(7,0,0)
