#https://leetcode.com/problems/reverse-string/

def reverseStringpy(s: str) -> str:
    return s[::-1]

def reverseString(s:str) -> str:
    lst = list(s)
    i,j=0,len(s)-1

    while i<j:
        lst[i],lst[j]=lst[j],lst[i]
        i+=1
        j-=1
    return lst



def main():
    print(reverseString("Damn"))


if __name__ == '__main__':
    main()
