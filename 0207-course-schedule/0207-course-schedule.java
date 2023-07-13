import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList<Integer>[] graph = new ArrayList[numCourses];
        for(int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }
        boolean[] visited = new boolean[numCourses];
        boolean[] stackFlag = new boolean[numCourses];

        // Create graph
        for(int i = 0; i < prerequisites.length; i++) {
            graph[prerequisites[i][1]].add(prerequisites[i][0]);
        }

        // Check cycle
        for(int i = 0; i < numCourses; i++) {
            if(cyclic(i, visited, stackFlag, graph)) {
                return false;
            }
        }
        return true;
    }

    private boolean cyclic(Integer i, boolean[] visited, boolean[] stackFlag, ArrayList<Integer>[] graph){
        // If StackFlag[i] is true, then a cycle found
        if (stackFlag[i]) return true;

        // If Visited[i] is true, then already processed. No need to DFS further.
        if (visited[i]) return false;

        visited[i] = true;

        // insert into the stack
        stackFlag[i] = true;

        // process all the neighbours
        for (Integer neighbor : graph[i]) {
            if (cyclic(neighbor, visited, stackFlag, graph)) return true;
        }

        // remove the element from stackFlag
        stackFlag[i] = false;

        return false;
    }
}
