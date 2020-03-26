class Solution {
    public int hIndex(int[] citations) {
        int h = 0;
        for (int i = citations.length-1; i >= 0; i--) {
            int number = citations.length - i;
            if(number <= citations[i]){
                h = Math.max(h, number);
            }else{
                break;
            }
        }
        return h;
    }
}