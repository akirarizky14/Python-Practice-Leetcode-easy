def isPalindrome(x):
        if x >= 0:
            c = str(x)[::-1]
            return(x == int(c))
        else:
            return False
print(isPalindrome(121))