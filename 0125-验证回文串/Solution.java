class Solution {
    public boolean isPalindrome(String s) {
        if(s.equals("")){ return true; }
        int i=0, j=s.length()-1;
        while(i < j){
            if(!(Character.isDigit(s.charAt(i)) || Character.isLetter(s.charAt(i)))){
                i++;    
            }else if(!(Character.isDigit(s.charAt(j)) || Character.isLetter(s.charAt(j)))){
                j--;
            }else if( (Character.isDigit(s.charAt(i)) && Character.isDigit(s.charAt(j)) && s.charAt(i) == s.charAt(j)) || 
                        (Character.isLetter(s.charAt(i)) && Character.isLetter(s.charAt(j)) && Character
                            .toUpperCase(s.charAt(i)) == Character.toUpperCase(s.charAt(j)) )){
                i++;
                j--;
            }else{
                return false;
            }

        }
        return true;
    }
}