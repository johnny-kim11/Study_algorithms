def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    print('fibo({}) + fibo({})'.format(n-1, n-2))
    
    return fibo(n-1) + fibo(n-2)

print(fibo(7))