def segregate_even_and_odds(A):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    n = len(A)
    j = 0

    for i in range(n):
        if A[i] % 2 == 0:
            A[i], A[j] = A[j], A[i]
            j += 1
    return A
