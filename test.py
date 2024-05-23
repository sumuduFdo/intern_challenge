def findSum(arr, num):
    if num <= 0:
        return 0
    else:
        print('num: ', num)
        value = findSum(arr, num - 1) + arr[num-1]
        print('num:', num, ' arr:', arr[num-1], ' value: ', value)
        return value

arr = [1,2,3,4,5]
num = len(arr)

sum = findSum(arr, num)
print('Find Sum Result: ', sum)