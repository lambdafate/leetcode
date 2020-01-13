class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] helper = new int[nums1.length + nums2.length];
        int index = 0, i, j;
        for(i=0, j=0; i<nums1.length && j<nums2.length ;){
            if(nums1[i] < nums2[j]){
                helper[index++] = nums1[i++];
            }else{
                helper[index++] = nums2[j++];
            }
        }
        if(i == nums1.length){
            while(j < nums2.length){
                helper[index++] = nums2[j++];
            }
        }else{
            while(i < nums1.length){
                helper[index++] = nums1[i++];
            }
        }

        // 这里要除以2.0, 确保得到的结果为double类型
        if( helper.length % 2 == 0){
            return (helper[helper.length/2] + helper[helper.length/2 - 1]) / 2.0;
        }
        return helper[helper.length/2];
    }


    public static void main(String[] args){
        int[] nums1 = new int[]{1, 2};
        int[] nums2 = new int[]{3, 4};
        System.out.println(new Solution().findMedianSortedArrays(nums1, nums2));
    }
}