def update_arrival(h ,m ,d ):
    """
        Actualiza la hora de llegada sumando minutos adicionales.

        >>> update_arrival(10, 45, 20)
        (11, 5)
        >>> update_arrival(12, 30, 60)
        (13, 30)
        >>> update_arrival(22, 0, 120)
        (0, 0)
        >>> update_arrival(23, 57, 5 + 24 * 60)
        (0, 2)
        """
    mt = h * 60 + m + d
    hf = mt // 60 % 24
    mf = mt % 60
    return hf, mf
if __name__ == "__main__":
    import doctest
    print(doctest.testmod())