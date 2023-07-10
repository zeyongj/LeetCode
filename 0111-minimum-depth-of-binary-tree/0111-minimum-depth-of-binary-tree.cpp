/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include<queue>
using namespace std;

class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root == NULL) return 0;
        
        queue<pair<TreeNode*, int>> q;
        q.push({root, 1});

        while(!q.empty()){
            TreeNode* node = q.front().first;
            int depth = q.front().second;
            q.pop();

            if(node->left == NULL && node->right == NULL){
                return depth;
            }

            if(node->left != NULL){
                q.push({node->left, depth + 1});
            }

            if(node->right != NULL){
                q.push({node->right, depth + 1});
            }
        }

        return -1;
    }
};
