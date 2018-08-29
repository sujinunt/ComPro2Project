"""
Instruction:
Complete the "YOUR CODE HERE" portion and add two more meaningful testcases to each of the function's doctests (except the first one).

To test these functions, use the following command:

python3 -m doctest assignment1.py
"""
def twenty_eighteen():
    """Come up with the most creative expression that evaluates to 2018,
    using only numbers and the +, *, and - operators.

    >>> twenty_eighteen()
    2018
    """
    "*** YOUR CODE HERE ***"
    return "20"+"18"
def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"
    def opposite(b):
        return not b
    def square(x):
        return x * x
    if(f=="square"):
        y=int(x)
        for i in range(n):
            y = square(y)
        return y
    else:
        if(x==0,"0"):
            return True
        else:
         for i in range(n):
            x = opposite(x)
         return x


def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    n = str(n);
    """get n to string"""
    digitSum = 0
    for i in n:
        digitSum += int(i)
        """Chang back to int and + all"""
    return digitSum

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    x = n.find("88")
    if (x == -1):
        return False
    else:
        return True




def a_plus_abs_b_try(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b_try(2, 3)
    5
    >>> a_plus_abs_b_try(2, -3)
    5
    """
    if b < 0:
        f = a+(-1*b)
    else:
        f = a+b
    return f

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = a+(-1*b)
    else:
        f = a+b
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    "*** YOUR CODE HERE ***"
    maxx = max(a, b, c)
    if (maxx == c):
        minn = max(a, b)
    elif (maxx == b):
        minn = max(a, c)
    elif (maxx == a):
        minn = max(c, b)
    return (maxx * maxx) + (minn * minn)


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    import math
    for i in range(2,math.ceil(math.sqrt(n))):
        if (n%i==0):
            return int(n/i)
    return 1

"""
1. Pick a positive integer n as the start.
2. If n is even, divide it by 2.
3. If n is odd, multiply it by 3 and add 1.
4. Continue this process until n is 1.

The number n will travel up and down but eventually end at 1. This sequence of values of n is often called a Hailstone sequence, Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence:
"""
def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 1
    print(int(n))
    if n>1:
        if n % 2 == 0:
            count+=hailstone(n/2)
        else:
            count+=hailstone((n*3)+1)
    return int(count)

"""
For the following problems, you have to write at least 5 testcases of your own.
"""

def is_leap_year(year):
    """Return True if year is a leap year, otherwise return False.

    *** YOUR DOCTESTS HERE ***
    >>> is_leap_year(2018)
    False
    >>> is_leap_year(2019)
    False
    >>> is_leap_year(2020)
    True
    """
    "*** YOUR CODE HERE ***"
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def interval_intersect(a, b, c, d):
    """Return True if the intervals [a,b] and [c,d] intersect and False otherwise.

        *** YOUR DOCTESTS HERE ***
      >>> interval_intersect(10, 12, 15, 18)
      False
      >>> interval_intersect(10, 12, 11, 18)
      True
      >>> interval_intersect(20, 28, 11, 18)
      True



    """
    "*** YOUR CODE HERE ***"
    if (c<=a or c>=a and c<=b and d>=b or d<=b and d>=a):
        return True
    else:
        return False