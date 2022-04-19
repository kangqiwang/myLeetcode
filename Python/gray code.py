
class Solution:
    def grayCode(self,n: int) -> List[int]:
        result,head=[0],1
        for i in range(n):
            for j in range(len(result)-1,-1,-1):
                result.append(head+result[j])
            head <<=1
        return result
