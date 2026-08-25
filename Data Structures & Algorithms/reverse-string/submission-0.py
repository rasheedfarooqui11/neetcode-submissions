class Solution:
    def reverseString(self, s: List[str]) -> None:
        temp = []
        for i in s[::-1]:
            temp.append(i)
        for i in range(len(s)):
            s[i] = temp[i]
        
        