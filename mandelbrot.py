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
    """
    creates a grid of complex numbers given a top left and bottom right corner and a step
    
    the region between the top left and bottom right corners are divided given the step 
    size. the individual grid points represent a complex number with a real and imaginary
    component.
    
    Parameters:
    top_left (complex): top left corner of the grid
    bottom_right (complex): bottom right corner of the grid
    step (float): The step size to determine the grids spacing

    Returns:
    np.ndarray: 2D array of the grid of complex numbers from the given inputs
    
    """
    
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

def get_escape_time_color_arr(
    c_arr: np.ndarray,
    max_iterations: int
) -> np.ndarray:
    """
    Figures out the color for each point in the grid of complex numbers.
    Each color depends on how fast the point "escapes" when we run the Mandelbrot iteration.
    Points that never escape get colored black. Points that escape faster are lighter.
    Parameters:
    c_arr : A 2D numpy array of complex numbers
    max_iterations : How many times we loop before deciding the point never escapes
    Returns: A 2D numpy array of floats in the range [0.0, 1.0] representing
        greyscale color values for each point
    """
    # Initialize z and escape_times arrays
    z = np.zeros_like(c_arr, dtype=np.complex128)

    # Keep track of when each point escapes
    escape_times = np.full(c_arr.shape, max_iterations + 1, dtype=int)

    # Mask to track which points haven't escaped yet
    mask = np.ones(c_arr.shape, dtype=bool)

    # Loop through iterations to check when points escape
    for iteration in range(max_iterations + 1):
        # Mandelbrot iteration: z = z**2 + c
        z[mask] = z[mask] * z[mask] + c_arr[mask]

        # Check which points escaped with (|z| > 2)
        escaped = np.abs(z) > 2

        # Record escape time only for points escaping this iteration
        newly_escaped = escaped & mask
        escape_times[newly_escaped] = iteration

        # Don't update if already escaped
        mask[newly_escaped] = False

    # Compute color values using the formula
    color_arr = (max_iterations - escape_times + 1) / (max_iterations + 1)
    return color_arr

