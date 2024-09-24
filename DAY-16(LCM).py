import math

def find_lcm(N, M):
    return abs(N * M) // math.gcd(N, M)

# Example usage
N = int(input("Enter the first number (N): "))
M = int(input("Enter the second number (M): "))
lcm = find_lcm(N, M)

print("The LCM of", N, "and", M, "is:", lcm)
