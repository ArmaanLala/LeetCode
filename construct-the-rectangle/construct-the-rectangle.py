class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if (area == 1):
            return [1,1]
        opt = sqrt(area)
        print(opt)
        opt = int(opt)
        while (area % int(opt) != 0 or opt == 1 or area/opt > opt):
            opt = int(opt)
            opt += 1
        return [int(opt), int(area/opt)]