
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.


def reverse(str):
    return str[::-1]

def palindrone():
    maxi = 0
    for i in range(999, 99, -1):
        for j in range(i,99,-1):
            if str(i*j) == reverse(str(i*j)) and i * j > maxi:
                maxi = i*j
    return maxi

palindrone()
