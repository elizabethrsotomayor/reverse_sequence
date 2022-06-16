def reverse_seq(n: int) -> list:
    """
    Return a list of integers from n to 1 where n>0
    :param n:
    :return:
    """
    return [n - 1 for n in range(n + 1, 1, -1)]
