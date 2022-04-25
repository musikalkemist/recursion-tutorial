def factorial(n: int) -> int:
    print(f"Entering factorial with n = {n}")
    if n == 1:
        print(f"\nReturning factorial for n = {n} -> 1")
        return 1
    current_factorial =  n * factorial(n-1)
    print(f"Returning factorial for n = {n} -> {current_factorial}")
    return current_factorial


if __name__ == "__main__":
    value = 4
    result = factorial(value)
    print(f"\nFactorial for {value} is {result}")