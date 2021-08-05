class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = {-1,-1};
        int i = 0;
        int j = nums.length - 1;
        
        while (i <= j) {
            if (nums[i] == target && nums[j] == target) {
                ans[0] = i;
                ans[1] = j;
                return ans;
            }
            
            if (nums[i] < target) {
                i++;
            }
            if (nums[j] > target) {
                j--;
            }
            
            
        }
        return ans;
    }
}