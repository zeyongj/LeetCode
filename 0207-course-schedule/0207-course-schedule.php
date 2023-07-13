class Solution {

    /**
     * @param Integer $numCourses
     * @param Integer[][] $prerequisites
     * @return Boolean
     */
    function canFinish($numCourses, $prerequisites) {
        $adj = [];

        for ($i = 0; $i < $numCourses; $i++) {
            $adj[$i] = [];
        }
        
        foreach ($prerequisites as $p) {
            $adj[$p[0]][] = $p[1];
        }

        $nodeToVisitedState = [];
        
        for ($i = 0; $i < $numCourses; $i++) {
            if ($this->detectCycleDFSRecursive($i, $adj, $nodeToVisitedState)) {
                return false;
            }
        }

        return true;
    }



    function detectCycleDFSRecursive($currentNode, $adj, &$nodeToVisitedState) {
        // Base cases
        $currentVisitedState = isset($nodeToVisitedState[$currentNode]) ? $nodeToVisitedState[$currentNode] : 0;
        // We're seeing a node again as part of one of its children recursive calls --> we have a cycle.
        if ($currentVisitedState == 1) {
            return true;
        }
        // We've already recursively explored all children of this node --> we can already determine that there is no cycle.
        elseif ($currentVisitedState == 2) {
            return false;
        }
    
        // Mark the node as currently being recursively explored (but not complete again) so that we can identify if one of its children recursive calls touches it again (and thus that we have a cycle)
        $nodeToVisitedState[$currentNode] = 1;
    
        foreach ($adj[$currentNode] as $neighbour) {
            $neighbourHasCycle = $this->detectCycleDFSRecursive($neighbour, $adj, $nodeToVisitedState);
            if ($neighbourHasCycle) {
                return true;
            }
        }
    
        // We're done recursively exploring its children - mark it as completely visited so we don't attempt to explore it again.
        $nodeToVisitedState[$currentNode] = 2;
        // We've explored the whole graph and haven't found a cycle!
        return false;
    }
}