class Solution:
    def countBits(self, n: int) -> List[int]:
        
        answer=[]
        for i in range(0,n+1):
            str_bin=bin(i).replace("0b","")
            answer.append(str_bin.count("1"))
        return(answer)
