# Input: arr[] = {3, 1, 2, 3, 8}
# Output: 3 1 8 2 3
#
# Input: arr[] = {9, 8, 7, 6, 5, 4}
# Output: 7 6 9 8 5 4

def maximize_median(arr,n):
    # print(n)

    if n%2!=0:
        maxElement = arr.index(max(arr))

        arr[maxElement],arr[n//2]=arr[n//2],arr[maxElement]

    else:
        maxElement1 = arr.index(max(arr))
        print(maxElement1)

        # find 2nd maximum element
        maxElement2 = arr.index(max(arr[0: maxElement1]))
        print(maxElement2)

        maxElement2 = arr.index(max(arr[maxElement2],max(arr[maxElement1 + 1:])))

        print(maxElement2)


        # swap position for median
        (arr[maxElement1],
         arr[n // 2]) = (arr[n // 2],
                         arr[maxElement1])
        (arr[maxElement2],
         arr[n // 2 - 1]) = (arr[n // 2 - 1],
                             arr[maxElement2])

    for i in range(0, n):
        print(arr[i], end=" ")

        # Driver code
if __name__ == "__main__":
    arr = [4, 8, 3, 1, 3, 7, 0, 4]
    n = len(arr)
    maximize_median(arr, n)





