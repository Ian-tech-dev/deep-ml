import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    if x >0:
        # Your code here
        g_val = 0
        h_val = 0
        for i,j in enumerate(g_coeffs):
            g_val += j*x**(len(g_coeffs)-i-1)
        for i,j in enumerate(h_coeffs):
            h_val += j*x**(len(h_coeffs)-i-1)
        #compute the value of h**2
        h_squared = h_val**2

        #compute the value of h_prime and g_prime 
        h_prime = 0
        g_prime = 0

        for i,j in enumerate(g_coeffs):
            g_prime += (len(g_coeffs)-i-1)*j*x**(len(g_coeffs)-i-2)
        for i,j in enumerate(h_coeffs):
            h_prime += (len(h_coeffs)-i-1)*j*x**(len(h_coeffs)-i-2)
        
        # compute the gradient 
        result = ((g_prime*h_val)-(g_val*h_prime))/h_squared

        return result
    else:
        return -1
    pass