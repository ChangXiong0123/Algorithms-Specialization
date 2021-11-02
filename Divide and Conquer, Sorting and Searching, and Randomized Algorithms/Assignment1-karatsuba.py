# karatsuba's algorithm
import math


def karatsuba(x, y):
    if x <= 100 or y <= 100:
        return x*y

    else:
        n = int(math.log10(x)/2.0 + 0.5)
        a = x//10**n
        b = x % (10**n)
        c = y//(10**n)
        d = y % (10**n)
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a+b, c+d) - ac - bd

        return (10**(2*n))*ac + (10**n)*ad_plus_bc + bd


if __name__ == "__main__":
    m = 3141592653589793238462643383279502884197169399375105820974944592
    n = 2718281828459045235360287471352662497757247093699959574966967627
    result = karatsuba(m, n)
    print(result)
