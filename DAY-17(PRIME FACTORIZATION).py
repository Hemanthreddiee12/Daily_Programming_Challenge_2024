def prime_factors(N):
    factors = []
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            factors.append(i)
            N //= i


    if N > 1:
        factors.append(N)
    
    return factors

N = int(input("Enter a number: "))
result = prime_factors(N)

print("Prime factors:", result)
