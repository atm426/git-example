import sys
# this comment is useless
def my_function(x: float, y: float) -> float:
    ''' takes in two floats (x,y) and returns
    their sum '''

    return x + y * z

sum = my_function( float(sys.argv[1]), float(sys.argv[2]) )
print("\n")
print(sum)
