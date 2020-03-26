class Solution {
    public int hIndex(int[] citations) {
        int h = Integer.MIN_VALUE;
        int left=0, right=citations.length-1;
        while(left<=right){
            int mid = left + (right-left)/2;
            int number = citations.length-mid;
            if(number <= citations[mid]){
                h = Math.max(h, number);
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        return h == Integer.MIN_VALUE ? 0: h;
    }
}