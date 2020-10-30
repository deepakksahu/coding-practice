#https://leetcode.com/problems/first-unique-character-in-a-string/

def firstunique(s: str) -> str:
    dict={}
    for i in s:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    for index in range(len(s)):
        if dict[s[index]]==1:
            return index
    return -1

def main():
    print(firstunique("leetcode"))


if __name__ == '__main__':
    main()
