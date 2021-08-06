public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int val = 0;
        int counter = 0;
        while (counter < 32) {
            val = val << 1;
            val = val + (n &1);      
            n = n >> 1;
            counter++;
        }
        return val;
    }
}