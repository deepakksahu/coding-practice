#https://rb.gy/clmnrv



def countMinSquares( n):
    if n <= 3:
        return n
    res = n
    for x in range(1, n + 1):
        temp = x * x;
        if temp > n:
            break
        else:
            res = min(res, 1 + countMinSquares(n - temp))
    return res;

print(countMinSquares(6))
