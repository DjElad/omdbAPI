def triple(n):
    return n ** 3


def find_nb(m):
    is_m = 0
    for n in range(1, 100000000000000000000000000):
        if is_m == m:
            return n-1
        elif is_m < m:
            is_m += triple(n)
        elif is_m > m:
            return -1


print(find_nb(1249304347057665601))