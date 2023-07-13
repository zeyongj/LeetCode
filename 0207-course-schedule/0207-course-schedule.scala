object Solution {
    def canFinish(numCourses: Int, prerequisites: Array[Array[Int]]): Boolean = {
        val inDegree = Array.fill(numCourses)(0)
        var graph = Map((0 until numCourses).map((_,Array[Int]())):_*)
        val visited = Array.fill(numCourses)(false)
        var queue = scala.collection.immutable.Queue[Int]()

        //init inDegree and graph
        for(i <- prerequisites.indices){
          val dad = prerequisites(i)(1)
          val son = prerequisites(i)(0)
          inDegree(son) += 1
          graph = graph + (dad -> graph(dad).:+(son))
        }

        //enqueue the vertexes which inDegree equals 0
        for(i <- inDegree.indices){
          if(inDegree(i) == 0)
            queue = queue.enqueue(i)
        }

        while(queue.nonEmpty){
          val curVertex = queue.dequeue._1
          visited(curVertex) = true
          queue = queue.dequeue._2

          //possible vertexes of current path
          val nextVertexes = graph(curVertex)
          nextVertexes.foreach(v => {
            //remove the edges that related to currentVertex
            inDegree(v) -= 1
            //path go through
            if(inDegree(v) == 0)
              queue = queue.enqueue(v)
          })
        }

        visited.forall(_ == true)
      }
}