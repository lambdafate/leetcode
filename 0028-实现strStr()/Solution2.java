class Solution {
    public int strStr(String haystack, String needle) {
        if (needle.equals("")) {
            return 0;
        }
        if (haystack.equals("")) {
            return -1;
        }
        for(int i=0; i<=(haystack.length()-needle.length()); i--){
            int hindex=i, nindex = 0;
            while(hindex<haystack.length() && nindex<needle.length() &&  haystack.charAt(hindex) == needle.charAt(nindex)){
                hindex++; nindex++;
            }
            if(nindex == needle.length()){ return i; }
        }
        return -1;
    }
}