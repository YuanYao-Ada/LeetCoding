package Tree.Medium;

class Solution {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        return help(postorder.length-1, inorder.length-1, 0, inorder, postorder);
    }
    
    public TreeNode help(int poStart, int inStart, int inEnd, int[] inorder, int[] postorder) {
        if (poStart < 0 || inStart < inEnd) {return null;}
        TreeNode root = new TreeNode(postorder[poStart]);
        int index = 0;
        for (int i=inStart; i>=inEnd; --i) {
            if (inorder[i] == postorder[poStart]) {
                index = i;
            }
        }
        root.right = help(poStart-1, inStart, index+1, inorder, postorder);
        root.left = help(poStart + index - inStart - 1, index-1, inEnd, inorder, postorder);
        return root;
    }
}