class SparseVector {
    
    int [] vector;
    SparseVector(int[] nums) {
        vector = nums;
    }
    
    int[] getVector() {
        return vector;
    }
    
	// Return the dotProduct of two sparse vectors
    public int dotProduct(SparseVector vec) {
        int val = 0;
        int[] itter = vec.getVector();
        
        for (int i = 0; i < this.vector.length; i++) {
            val += (itter[i] * this.vector[i]);
        }
        return val;
    }
}

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1 = new SparseVector(nums1);
// SparseVector v2 = new SparseVector(nums2);
// int ans = v1.dotProduct(v2);