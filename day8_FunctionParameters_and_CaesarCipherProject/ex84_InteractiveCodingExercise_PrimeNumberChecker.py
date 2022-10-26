def prime_checker(number):
    for denominator in range(2, number):
        if number % denominator == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
