import sys

# read number of test cases, return an integer
def get_test_count():
    try:
        num_tests = int(sys.stdin.readline().strip())
    except ValueError:
        sys.stderr.write("ERROR: No. of test cases must be an integer")
        sys.exit(1)

    if (num_tests <= 0 or num_tests >100):
        sys.stderr.write("ERROR: No. of test cases [N] must satisfy 0 <= N <= 100")
        sys.exit(1)

    return num_tests

def get_inputs():
    try:
        count = int(sys.stdin.readline().strip())
        values = list(map(lambda x: int(x), sys.stdin.readline().strip().split(" ")))
    except ValueError:
        sys.stderr.write("ERROR: Invalid inputs")
        sys.exit(1)

    """ Input Validation:
        * check if count lies between 0 and 100
        * check if num. of values is consistent with count
    """
    if(count <= 0 or count>100 or count != len(values)):
        sys.stderr.write("ERROR: Invalid inputs")
        sys.exit(1)
    
    return count, values

def calcualte_square_sum(count, arr):
    if count <= 0:
        return 0
    else:
        if arr[count - 1] < 0:
            return calcualte_square_sum(count - 1, arr) + 0
        
        return calcualte_square_sum(count - 1, arr) + arr[count - 1]**2

def print_output(arr):
    if len(arr) == 0:
        return
    else:
        print(arr[0])
        print_output(arr[1:])

def calculate(num_tests, arr):
    if num_tests == 0:
        print_output(arr)
        return 0
    else:
        count, values = get_inputs()
        arr.append(calcualte_square_sum(count, values))
        return calculate(num_tests - 1, arr)
        

def main():
    num_tests = get_test_count()
    calculate(num_tests, [])

if __name__ == '__main__':
    main()
