def subtract(a, b, c):
    """
      >>> subtract(3, 5, 4)
      2
      >>> subtract(10, 29, 14)
      -5
      >>> subtract(99 ,8 , 20)
      111
    """
    
    return a - (b - c)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
