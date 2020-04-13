class Solution {
    public String convert(String s, int numRows) {
        if(numRows < 2 || s.length() < 3){
            return s;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numRows; i++) {
            for(int j=i; j<s.length();){
                sb.append(s.charAt(j));
                j += (numRows - 1 - i) * 2;
                if(i==0 || i==numRows-1){
                    j += 2*i;
                    continue;
                }
                if(j >= s.length()){
                    break;
                }
                sb.append(s.charAt(j));
                j += 2*i;
            }
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println("Hello\n");
        String res = new Solution().convert("LEETCODEISHIRING", 3);
        System.out.println(res);
    }
}