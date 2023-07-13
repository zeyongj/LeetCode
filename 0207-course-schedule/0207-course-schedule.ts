function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    const preCourses: number[][] = []; 
    const coursesTaken = new Set<number>();

    for(let i=0; i<numCourses; i++){
        preCourses.push([]);
    }

    for(const prerequisite of prerequisites){
        const preCourse = prerequisite[1];
        const course = prerequisite[0];
        preCourses[course].push(preCourse);
    }

    let takeNewCourse = true;
    while(takeNewCourse){
        takeNewCourse = false;
        for(let i=0; i<numCourses; i++){
            if(coursesTaken.has(i)){
                continue;
            }
            let canTake = true;
            for(const preCourse of preCourses[i]){
                if(!coursesTaken.has(preCourse)){
                    canTake = false;
                }
            }
            if(canTake){
                coursesTaken.add(i)
                takeNewCourse = true;
            }
        }
    }

    return coursesTaken.size===numCourses;
};