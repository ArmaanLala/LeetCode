class Solution:
    def reverseWords(self, s: str) -> str:
        # arr = s.split(' ')[::-1]
        # arr = [i for i in arr if i !='']
        # return ' '.join(arr).strip()
    
        return ' '.join([i for i in s.split(' ')[::-1] if i !=''])