class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {']':'[', '}':'{', ')':'('}
        for c in s:
            if c in pairs.values():
                seen.append(c)
            elif not seen or pairs[c] != seen.pop():
                return False
        return not seen
                    
            

        