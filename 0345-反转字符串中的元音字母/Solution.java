class Solution {
    public String reverseVowels(String s) {
        if(s == null || s.length() == 0){ return s; }
        char[] chars = s.toCharArray();
        int i=0, j=s.length()-1;
        while(i < j){
            if(!istarget(chars[i])){
                i++; continue;
            }
            if(!istarget(chars[j])){
                j--; continue;
            }
            char temp = chars[i];
            chars[i++] = chars[j];
            chars[j--] = temp;
        }
        return String.valueOf(chars);
    }

    private boolean istarget(char c){
        c = Character.toLowerCase(c);
        return c=='a' || c=='o' || c=='e' || c=='i' || c=='u';
    }
}