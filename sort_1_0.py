# https://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/

# Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


def bf_segregate0and1(arr, n):
    # Counts the no of zeros in arr
    count = 0

    for i in range(0, n):
        if (arr[i] == 0):
            count = count + 1

    # Loop fills the arr with 0 until count
    for i in range(0, count):
        arr[i] = 0

    # Loop fills remaining arr space with 1
    for i in range(count, n):
        arr[i] = 1


def opt_segregate0and1(arr, n):
    left, right = 0, n - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 0 and left < right:
            right -= 1
        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1
    return arr


def opt2_segregate0and1(arr, size):
    type0 = 0
    type1 = size - 1

    while (type0 < type1):
        if (arr[type0] == 1):
            (arr[type0],arr[type1]) = (arr[type1],arr[type0])
            type1 -= 1
        else:
            type0 += 1


# Function to print segregated array
def print_arr(arr, n):
    print("Array after segregation is ", end="")

    for i in range(0, n):
        print(arr[i], end=" ")


def main():
    arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]# [0, 1, 0, 1, 1, 1]
    n = len(arr)
    # bf_segregate0and1(arr,n)
    # opt_segregate0and1(arr, n)
    opt2_segregate0and1
    print_arr(arr, n)


if __name__ == '__main__':
    main()
