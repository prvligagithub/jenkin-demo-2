import sys


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    # Simplified fallback: if numbers aren't provided, default to 0
    if len(sys.argv) == 3:
        try:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
        except ValueError:
            print("Error: Command line arguments must be integers.")
            sys.exit(1)
    else:
        # Prevents the error if you just type "python add.py" or click play
        num1 = 0
        num2 = 0

    result = add_numbers(num1, num2)

    print("=================================")
    print("Addition Result")
    print("=================================")
    print(f"First Number : {num1}")
    print(f"Second Number: {num2}")
    print(f"Sum          : {result}")
