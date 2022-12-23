class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int a = m - 1;
        int b = n - 1;
        for(int i = nums1.length - 1; b >= 0; i--){
            if(i >= 0 && a >= 0 && nums1[a] > nums2[b]){
                nums1[i] = nums1[a--];
            }
            else{
                nums1[i] = nums2[b--];
            }
        }
    }
}