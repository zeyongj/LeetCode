impl Solution {
     pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
      let mut graph = vec![vec![]; num_courses as usize];
      let visited = &mut vec![0; num_courses as usize];
      for pre in prerequisites {
       let (x, y) = (pre[0], pre[1]);
       graph[x as usize].push(y);
      }
      for i in 0..num_courses {
       if !Solution::depth_first_search(graph.to_vec(), visited, i as usize) {
        return false;
       }
      }

      true
     }

     pub fn depth_first_search(graph: Vec<Vec<i32>>, visited: &mut Vec<i32>, i: usize) -> bool {
      if visited[i] == -1 {
       return false;
      } else if visited[i] == 1 {
       return true;
      }
      visited[i] = -1;
      for j in graph[i].to_vec() {
       if !Solution::depth_first_search(graph.to_vec(), visited, j as usize) {
        return false;
       }
      }
      visited[i] = 1;
      true
     }
}