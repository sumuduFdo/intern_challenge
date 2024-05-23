import sys


def square(num: int):
    return num * num


def calculateSquareSum(count, arr):
    if count <= 0:
        return 0
    else:
        num = int(arr[count - 1])
        if num < 0:
            return calculateSquareSum(count - 1, arr) + 0
        else:
            return calculateSquareSum(count - 1, arr) + square(num)


def main():
    while True:
        # read input from the standard input
        line1 = sys.stdin.readline().strip()
        line2 = sys.stdin.readline().strip()

        # validate the first input is a single integer
        if not line1.isdigit():
            print("ERROR: Invalid input, input 1 must be an integer.")
            continue

        # validate the second input contains only numbers -> positive & negative
        if not (line2.replace(" ", "").replace("-", "")).isdigit():
            print("ERROR: Invalid input, input 2 must contain only [+/-] numbers.")
            continue

        # validate the consistency of inputs
        # check if number of values in second input == first input
        if len(line2.split(" ")) != int(line1):
            print('ERROR: Inconsistent inputs.')
            continue

        print(calculateSquareSum(int(line1), line2.split(" ")))


if __name__ == '__main__':
    main()