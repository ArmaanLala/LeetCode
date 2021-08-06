class Solution {
    public List<Integer> pancakeSort(int[] arr) {
        List<Integer> list = new LinkedList<>();
        if (arr.length == 0) {
            return list;
        }
        int min = arr[0];
        int pos = 0;
        int max;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < min) {
                min = arr[i];
                pos = i;
            }
        }
        pancakeFlip(pos + 1, arr);
        list.add(pos + 1);
        
        
        max = arr[0];
        pos = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
                pos = i;
            }
        }
        pancakeFlip(pos + 1, arr);
        list.add(pos + 1);
        
        pancakeFlip(arr.length, arr);
        list.add(arr.length);
        int count = 1;
        while (!isSorted(arr)) {
            max = min;
            for (int i = 0; i < arr.length - count; i ++) {
                if (arr[i] > max) {
                    max = arr[i];
                    pos = i;
                }
                
            }
            pancakeFlip(pos + 1, arr);
            list.add(pos + 1);
            // System.out.println("About to flip: " + (arr.length - count));
            pancakeFlip(arr.length - count, arr);
            list.add(arr.length - count);
            count++;
        }
    
        
        return list;
    }
    
    private void pancakeFlip(int x, int[] arr) {
        int temp;
        for (int i = 0; i <= (x-1)/2; i++) {
            temp = arr[i];
            arr[i] = arr[x - 1 - i];
            arr[x - 1 - i] = temp;
        }
        // for (int t : arr) {
        //     System.out.println(t);
        // }
        
    }
    
    private boolean isSorted(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i - 1] > arr[i]) {
                return false;
            }
        }
        return true;
    }
}