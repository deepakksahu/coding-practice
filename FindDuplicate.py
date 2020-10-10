"""Take a text file which contains list of DBs and give the cummulative sum for each db reading the specific size field"""
"""In line number 32 just replace it with the list text file location.Extension should be .txt"""


import json
import os


def printRepeating(arr, size):
    print("The repeating elements are: ")

    for i in range(0, size):

        if arr[abs(arr[i])] >= 0:
            print(arr[abs(arr[i])])
            print("""...""")
            arr[abs(arr[i])] = -arr[abs(arr[i])]
            print(arr[abs(arr[i])])
            print("")

        else:
            print(abs(arr[i]), end=" ")
def main():
    if __name__ == '__main__':
        arr=[3, 1, 3, 4, 2]
        printRepeating(arr,4)
        # print(abs(-3))
main()