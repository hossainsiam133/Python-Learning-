def prime_factors(n):
    factors = []
    # Handle 2 separately
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Handle odd numbers
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2

    # If remaining n is a prime
    if n > 1:
        factors.append(n)

    return factors

# Pretty print
def print_factorization(n):
    factors = prime_factors(n)
    formatted = " × ".join(str(f) for f in factors)
    print(f"{n} = {formatted}")

# Example: Factorize numbers from 2 to 100
for i in range(101, 1001):
    print_factorization(i)
