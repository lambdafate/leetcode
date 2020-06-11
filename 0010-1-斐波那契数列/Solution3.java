public class Solution3 {
    
    public int fib(int n) {
        if(n < 2){
            return n;
        }
        int n1 = 0, n2 = 1;
        while(n-- != 0){
            int temp = n2;
            n2 = (n1 + n2) % 1000000007;
            n1 = temp;
        }
        return n1;
    }


}