#https://leetcode.com/problems/valid-palindrome/https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s: str) -> bool:
    check_str="".join(e for e in s if e.isalnum()).lower()
    print(check_str)
    print(check_str[::-1])
    return check_str==check_str[::-1]

def main():
    print(isPalindrome("A man, a plan, a canal: Panama"))


if __name__ == '__main__':
    main()
