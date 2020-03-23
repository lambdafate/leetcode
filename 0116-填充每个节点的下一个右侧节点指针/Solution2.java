
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {
    }

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};

public class Solution {
    public Node connect(Node root) {
        helper(root);
        return root;
    }
    private void helper(Node root){
        if(root == null || root.left == null){ return; }
        helper(root.left);
        helper(root.right);
        Node p=root.left, q=root.right;
        while(p != null){
            p.next = q;
            p = p.right;
            q = q.left;
        }
    }
}