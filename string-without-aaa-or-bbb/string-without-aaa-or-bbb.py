class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        string = ""
        count = 0 
        while (a != 0 or b != 0):
            print("A: " + str(a) + " B : " + str(b))
            if (a > b and a > 0) :
                if (count - 2 >= 0):
                    if not(string[count-1] == "a" and string[count-2] == "a"):
                        string += "a"
                        a -= 1
                    elif (b > 0):
                        string += "b"
                        b-=1
                else:
                    string += "a"
                    a -= 1
            elif ( b > 0) :
                if (count - 2 >= 0):
                    if not(string[count-1] == "b" and string[count-2] == "b"):
                        string += "b"
                        b -= 1
                    elif (a > 0):
                        string += "a"
                        a-=1
                else:
                    string += "b"
                    b -= 1
            
            
            count += 1
        return string