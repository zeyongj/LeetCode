// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::VecDeque;

type Node = Rc<RefCell<TreeNode>>;

//  Breath For Search 

impl Solution {
    pub fn min_depth(root: Option<Node>) -> i32 {

        if root.is_none() { 
            return 0 
        }
        let mut q = VecDeque::new();
        //  append root node to q
        //  (level, node)
        q.push_back((1, root.clone()));

        while !q.is_empty() { 
            if let Some((level, Some(node))) =  q.pop_front() { 
                let node = node.borrow();
                //  Check whether a left or right node exist 
                if node.left.is_none() && node.right.is_none() { 
                    return level
                } 
					//**Can be optimised using if let syntax here
                //  Add left node 
                if node.left.is_some() { 
                    q.push_back((level + 1, node.left.clone()));
                } 
                //  Add right node 
                if node.right.is_some() {
                    q.push_back((level + 1, node.right.clone()))

                }
            }
        }
      0
    }
}