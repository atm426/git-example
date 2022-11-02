import sys
# this comment is useless
# so is this one
def my_function(x: float, y: float) -> float:
    ''' takes in two floats (x,y) and returns
    their sum '''
    return x + y

sum = my_function( float(sys.argv[1]), float(sys.argv[2]) )
print("\n")
print(sum)
