import math

def count_divisors(N):
    count = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            count += 1  
            if i != N // i:
                count += 1  
    return count

N = int(input("Enter a number: "))
result = count_divisors(N)

print("Number of divisors:", result)
