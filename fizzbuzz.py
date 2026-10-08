"""Classic FizzBuzz implementation with self-tests.

Rules:
    - If n is divisible by 3 -> "Fizz"
    - If n is divisible by 5 -> "Buzz"
    - If n is divisible by both 3 and 5 -> "FizzBuzz"
    - Otherwise -> str(n)
"""


def fizzbuzz(n: int) -> str:
    """Return the FizzBuzz string for a single integer n.

    Args:
        n: A positive integer (1..n in the classic problem).

    Returns:
        "FizzBuzz" if divisible by both 3 and 5,
        "Fizz" if divisible by 3 only,
        "Buzz" if divisible by 5 only,
        otherwise the number as a string.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


if __name__ == "__main__":
    # Self-tests: verify correctness across the four branches.
    assert fizzbuzz(1) == "1", "fizzbuzz(1) should be '1'"
    assert fizzbuzz(3) == "Fizz", "fizzbuzz(3) should be 'Fizz'"
    assert fizzbuzz(5) == "Buzz", "fizzbuzz(5) should be 'Buzz'"
    assert fizzbuzz(15) == "FizzBuzz", "fizzbuzz(15) should be 'FizzBuzz'"
    assert fizzbuzz(100) == "Buzz", "fizzbuzz(100) should be 'Buzz'"
    assert fizzbuzz(9) == "Fizz", "fizzbuzz(9) should be 'Fizz'"
    assert fizzbuzz(7) == "7", "fizzbuzz(7) should be '7'"
    assert fizzbuzz(30) == "FizzBuzz", "fizzbuzz(30) should be 'FizzBuzz'"

    print("All FizzBuzz tests passed!")
