class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allUper = word.upper()
        allLower = word.lower()
        first = word.lower()
        first = first[0].upper() + first[1:]
        return (word == allUper or word == allLower or word == first)