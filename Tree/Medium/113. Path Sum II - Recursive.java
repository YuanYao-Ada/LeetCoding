package Tree.Medium;

import java.util.LinkedList;
import java.util.List;

/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode(int x) { val = x; } }
 */
class Solution {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) {val = x;}
    }

    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> result = new LinkedList<>();
        LinkedList<Integer> subList = new LinkedList<>();
        helper(root, sum, subList, result);
        return result;
    }
    
    public void helper(TreeNode node, int sum, LinkedList<Integer> subList, List<List<Integer>> result) {
        if (node == null) {return;}
        subList.add(node.val);
        if (node.left == null && node.right == null && node.val == sum) {
            result.add(new LinkedList(subList)); 
        }
        helper(node.left, sum - node.val, subList, result);
        helper(node.right, sum - node.val, subList, result);
        subList.removeLast();
    }
}