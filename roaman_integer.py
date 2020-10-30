# https://leetcode.com/problems/roman-to-integer/

def romantoInteger(s: str) -> int:
    d = {"I": 1,
         "V": 5,
         "X": 10,
         "L": 50,
         "C": 100,
         "D": 500,
         "M": 1000}
    result, prev = 0, 0
    for i in s[::-1]:
        # print(i)
        # print(prev)
        if d[i] >= prev:
            result += d[i]
        else:
            result -= d[i]
        prev = d[i]
    return result


def main():
    print(romantoInteger("IL"))


if __name__ == '__main__':
    main()
