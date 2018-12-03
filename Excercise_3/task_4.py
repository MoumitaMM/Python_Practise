'''
Is Prime? 
A prime number (or just a prime) is a natural number which has exactly two factors, i.e. 1 and
itself. It follows that if any number n has a factor greater than 1 and smaller than n, then it cannot
be prime, as it would have at least three factors.

Note: 1 is not prime, while 2 (factors: {1, 2}) and 3 (factors: {1, 3}) for example are. 0 and
negative numbers are not prime, so your code should handle these cases as well.
'''

is_prime = True

n=int(input('Please input a number :'))
chk_cnt=0
if n >0:
    if n==1:
        is_prime = False
    else:
        for i in range(1,n+1):
            chk=n/i
            if chk.is_integer():
                chk_cnt+=1
        if chk_cnt==2:
            is_prime = True
        else:
            is_prime = False
else:
    is_prime = False

print('Is the input number prime ?',is_prime)


