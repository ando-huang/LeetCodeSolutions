/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root==null) {
            return true;
        }
        if (root.left == null && root.right == null) {
            return true;
        }
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    private boolean isValidBST(TreeNode root, long min, long max) {
        if (root==null) {
            return true;
        }
        boolean minCheck = true;
        boolean maxCheck = true;

        if (root.val > min) {
            minCheck = true;
        } else {
            minCheck = false;
        } 
        
        
        if (root.val < max) {
            maxCheck = true;
        } else {
            maxCheck = false;
        } 
        


        if (minCheck && maxCheck) {
            return (isValidBST(root.left, min, root.val) &&
                isValidBST(root.right, root.val, max));
        }
        return false;
    }
}