class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        while(True):    
            newStr = ''
            for i in range(len(dominoes)):
                if (dominoes[i] == '.'):
                    lVar = (dominoes[i+1] == 'L') if (i+1 in range(len(dominoes))) else False
                    rVar = (dominoes[i-1] == 'R') if (i-1 in range(len(dominoes))) else False
                    if (lVar and not rVar):
                        newStr += 'L'
                    elif (rVar and not lVar):
                        newStr += 'R'
                    else:
                        newStr += '.'
                else :
                    newStr += dominoes[i]
            if (dominoes == newStr):
                return dominoes
            dominoes = newStr