class Solution {
    public int findUnsortedSubarray(int[] nums) {
        
        int[] cpyNums = nums.clone();
        
        Arrays.sort(nums);
        int start = -1, end = -1;
        
        for (int i = 0; i < nums.length; i ++) {
            if (nums[i] != cpyNums[i] && start == -1) {
                start = i;
            } else if (nums[i] != cpyNums[i]) {
                System.out.println(i);
                end = i;
            }
        }
        if (start == -1 && end == -1) {
            return 0;
        }
        if (end - start >= 0) {
            return end - start + 1;
        }
        return 0;
        
    }
}