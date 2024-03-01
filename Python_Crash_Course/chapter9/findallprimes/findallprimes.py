def primes(n:int)->list[int]:
    prime_list:list[int] = []
    for num in range(2, n + 1):  # Start from 2 since 1 is not a prime number
        is_prime:bool = True
        for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to square root of num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    return prime_list

# Example usage:
 
 
