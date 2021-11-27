# define a function that takes an input, squares it, adds 7, then returns the answer
def x2p7(x):
    """    this is my documentation string
    it needs to be in triple double quotes
    this function returns x^2 + 7"""
    y = x*x
    z = y+7
    return z

print('x^2 + 7 = ',x2p7(5))
print(x2p7.__doc__)
