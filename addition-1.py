import sys


def main():
    # sys.argv[0] is the script name
    # sys.argv[1] is the first argument (NUM1)
    # sys.argv[2] is the second argument (NUM2)
    if len(sys.argv) < 3:
        print("Error: Missing arguments. Expected two numbers.")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        print("Error: Please provide valid numbers.")
        sys.exit(1)


if __name__ == "__main__":
    main()
