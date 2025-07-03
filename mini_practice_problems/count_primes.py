def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def count_primes(num):
    count = 0
    for n in range(1,num+1):
        if is_prime(n):
            count += 1
    return count


print(count_primes(5))





