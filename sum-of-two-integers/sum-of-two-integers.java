class Solution {
    public int getSum(int a, int b) {
        int c;
        while (b!= 0) {
            int xor = a^b;
            c = (a&b) <<1;
            a = xor;
            b = c;
        }
        return a;
    }
}