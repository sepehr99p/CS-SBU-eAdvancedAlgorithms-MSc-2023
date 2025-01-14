from math import ceil, floor


def karatsuba(X, Y):
    # Base case
    if X < 10 and Y < 10:
        return X * Y

    # determine the size of X and Y
    size = max(len(str(X)), len(str(Y)))

    # Split X and Y
    n = ceil(size // 2)
    p = 10 ** n
    a = floor(X // p)
    b = X % p
    c = floor(Y // p)
    d = Y % p

    # Recur until base case
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    e = karatsuba(a + b, c + d) - ac - bd

    # return the equation
    return int(10 ** (2 * n) * ac + (10 ** n) * e + bd)


if __name__ == '__main__':
    print("Final value is :",karatsuba(2023,3003))
