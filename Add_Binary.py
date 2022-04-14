class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=int(a,2)
        y=int(b,2)
        s=x+y
        bin_str=bin(s)
        final=bin_str.replace("0b","")
        
        return(final)
