import java.util.Stack;

class Solution {
    public boolean backspaceCompare(String S, String T) {
        Stack<Character> stackS = new Stack<>();
        Stack<Character> stackT = new Stack<>();

        int index = 0;
        while(index < S.length()){
            if(S.charAt(index) != '#'){
                stackS.push(S.charAt(index));
            }else if(!stackS.isEmpty()){
                stackS.pop();
            }
            index++;
        }
        index = 0;
        while (index < T.length()) {
            if (T.charAt(index) != '#') {
                stackT.push(T.charAt(index));
            } else if (!stackT.isEmpty()) {
                stackT.pop();
            }
            index++;
        }
        if(stackS.size() != stackT.size()){ return false; }
        while( !stackS.isEmpty() && !stackT.isEmpty() ){
            if(stackS.pop() != stackT.pop()){
                return false;
            }
        }
        return stackS.size() == stackT.size();
    }
}