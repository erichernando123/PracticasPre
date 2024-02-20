def cercanias(lin,sen):

   """
    >>> cercanias(3,'N')
    12
    >>> cercanias(7,'N')
    0
    >>> cercanias(4,'S')
    15
    >>> cercanias(2,'W')
    0
    """
   if lin == 1 and sen == 'N':
       return 8
   elif lin == 1 and sen == 'S':
       return 7
   elif lin ==2 and sen == 'N':
       return 10
   elif lin == 2 and sen == 'S':
       return 9
   elif lin == 3 and sen == 'N':
       return 12
   elif lin == 3 and sen == 'S':
       return 13
   elif lin == 4 and sen == 'N':
       return 14
   elif lin == 4 and sen == 'S':
       return 15
   else:
       return 0
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
