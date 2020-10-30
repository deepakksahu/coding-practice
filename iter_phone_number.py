#https://www.geeksforgeeks.org/find-possible-words-phone-digits/
#https://www.geeksforgeeks.org/iterative-letter-combinations-of-a-phone-number/
# Input number: 234
# Output:
# adg adh adi aeg aeh aei afg afh
# afi bdg bdh bdi beg beh bei bfg
# bfh bfi cdg cdh cdi ceg ceh cei
# cfg cfh cfi

# hashTable[i] stores all characters
# that correspond to digit i in phone
hashTable = ["", "", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]


# A recursive function to print all
# possible words that can be obtained
# by input number[] of size n. The
# output words are one by one stored
# in output[]
def printWordsUtil(number, curr, output, n):
    if (curr == n):
        print(output)
        return

    # Try all 3 possible characters
    # for current digit in number[]
    # and recur for remaining digits
    for i in range(len(hashTable[number[curr]])):
        print(hashTable[number[curr]])
        print(hashTable[number[curr]][i])
        output.append(hashTable[number[curr]][i])
        printWordsUtil(number, curr + 1, output, n)
        output.pop()
        if (number[curr] == 0 or number[curr] == 1):
            return;

        # A wrapper over printWordsUtil().


# It creates an output array and
# calls printWordsUtil()
def printWords(number, n):
    printWordsUtil(number, 0, [], n)


# Driver function
if __name__ == '__main__':
    number = [2, 3]
    n = len(number)
    printWords(number, n);

# This code is contributed by prajmsidc
