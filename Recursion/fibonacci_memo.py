memo = [-1 for _ in range(10)]

def fibo(n):
    if n == 1 or n == 2:
        return 1
    
    print('fibo({}) + fibo({})'.format(n-1, n-2))
    if memo[n-1] != -1:
        ans1 = memo[n-1]
    else:
        ans1 = fibo(n-1)
        memo[n-1] = ans1
        
    if memo[n-2] != -1:
        ans2 = memo[n-2]
    else:
        ans2 = fibo(n-2)
        memo[n-2] = ans2
    
    result =  ans1 + ans2
    # print(memo)
    return result

print(fibo(7))
print(memo)
