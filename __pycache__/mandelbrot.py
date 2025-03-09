import math
import numpy as np

def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """
    Calculates the escape time given an initial complex value c and the 
    maximum amount of iterations allowed
    
    the escape time occurs when the value of |zn| is greater than or equal to 2 
    given the equation zn = zn^2 + c
    
    If zn does not escape within the set amount of max_iterations the function returns 
    none. If zn does escape, the function returns that amount of iterations before escaping
    
    Parameters:
    c (complex): A given complex number
    max_iterations (int): The maximum number of iterations allowed before escaping
    
    Returns:
    int | None: The amount of iterations before the point escaped of None is it did not 
    escape in the given max_iterations.
    """
    
    zn = 0
    # for loop that repeats max_iterations amount of time
    for i in range(max_iterations): 
        # formula for each iteration of zn
        zn = (zn)**2 + c 
        if abs(zn) >= 2: # if zn escaped
            return i # returns number of iterations taken
    return None #zn did not escape
    
def get_complex_grid(
    top_left: complex,
    bottom_right: complex,
    step: float) -> np.ndarray:
    
    #calculates real ranges for the grid
    real_range = np.arange(top_left.real, bottom_right.real, step) 
    #calculates imaginary ranges for the grid
    imag_range = np.arange(top_left.imag, bottom_right.imag, -step)
    
    # determines the dimensions of the grip (rows x cols)
    rows = len(imag_range) 
    cols = len(real_range)
    
    # Creates an empty grid of zeros of height rows and width cols
    grid = np.zeros((rows, cols))
    
    # uses broadcasting to multiply two reshaped grids with a height a 1 and a width of 1
    grid = real_range.reshape(1, cols) + 1j * imag_range.reshape(rows, 1)
    return grid
