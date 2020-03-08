package Tree.Medium;

import java.util.ArrayList;
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
        TreeNode(int x) { val = x; }
    }

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        helper(result, root, 0);
        return result;
    }
    
    public void helper(List<List<Integer>> result, TreeNode node, int depth) {
        if (node == null) return;
        if (depth >= result.size()){
            result.add(new LinkedList<Integer>());
        }
        if (depth % 2 == 0) {
            result.get(depth).add(node.val);
        } else {
            result.get(depth).add(0, node.val);
        }
        helper(result, node.left, depth+1);
        helper(result, node.right, depth+1);
    }
}