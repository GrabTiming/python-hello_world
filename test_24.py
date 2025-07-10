import math


primes = []
is_prime  = [True] * 1000001


def sieve():
    global is_prime
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, 1000001):
        if is_prime[i]:
            primes.append(i)
            for j in range(len(primes)) :
                if i * primes[j] > 1000001:
                    break
                is_prime[i*primes[j]] =  False
                if i % primes[j] == 0:
                    break

def main():
    sieve()
    for i in range(20):
        print(primes[i])

if __name__ == "__main__":
    main()
