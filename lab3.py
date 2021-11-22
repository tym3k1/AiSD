def fib(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return  fib(n-1) + fib(n-2)

def power(number: int, n: int) -> int:
    if n <= 1: return number
    return power(number, n - 1) * number

def reverse(txt: str) -> str:
    if len(txt) == 0: return txt
    return reverse(txt[1:]) + txt[0]

def factorial(n: int) -> int:
    if n <= 1: return 1
    return factorial(n-1)*n

def prime(n: int) -> bool:
    i = 2
    if n <= 2: return True if n == 2 else False
    if n % i == 0: return False
    if i * i > n:return True
    return prime(n, i + 1)

""" def n_sums(n: int) -> list[int]: """
    


""" 
    res = [int(x) for x in str(n)]
    resEven = [x for x in res if x%2==0]
    resOdd = [x for x in res if x%2!=0]
    even = sum(resEven)
    odd = sum(resOdd)
    if even == odd: list.append(n)
    return n_sums(n-1)
 """

 
def only_odd(L):
    return L[0:L[0]&1]+only_odd(L[1:]) if L else L


only_odd(3)