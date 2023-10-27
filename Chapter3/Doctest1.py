"""
  >>> type(thing1)
  <class 'list'>
  >>> type(thing2)
  <class 'tuple'>
  >>> type(thing3)
  <class 'str'>




"""

thing1 = [1, 2, 3, 4]
thing2 = (5, 6, 7, 8)
thing3 = ("Hello world")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
