class Solution {
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
                                                
              var array = Array(repeating:[Int](),count:numCourses)
              var indegrees = Array(repeating:0,count:numCourses)
                                                
            for course in prerequisites {
            var tempo:[Int] = array[course[1]]
            tempo.append(course[0])
            array[course[1]] = tempo
            indegrees[course[0]] += 1
            }
            
            var que = [Int]()
            for index in 0..<numCourses {
                if indegrees[index] == 0 {
                que.insert(index, at: 0)
                  }
                }
                var count = numCourses
                while que.count > 0 {
                let current = que.removeLast()
                count -= 1
                let adj = array[current]
                for course in adj {
                indegrees[course] -= 1
                if indegrees[course] == 0 {
                que.insert(course, at: 0)
                   }
                }
            }
                                                
            if count == 0 {
            return true
            } else {
            return false
            }
        }
}