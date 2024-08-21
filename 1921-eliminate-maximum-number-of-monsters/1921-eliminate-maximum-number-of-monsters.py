class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        #deducing the time to reach in the city for every monster
        for i in range(len(dist)): dist[i]/=speed[i]  


        # number of monster have to kill before ith minute
        haveToKill = [0 for i in dist]

        for x in dist:

            if ceil(x)<len(dist):

                haveToKill[ceil(x)]+=1
                #have to kill this monster before the time of ceil(x)
                #if ceil(x)>=len(dist) or n that means it already been killed cz, you already fired n shots


                
        for i in range(len(speed)):

            #calculating the total monster that needed to be killed before i minute
            if i>0: haveToKill[i]+=haveToKill[i-1]

    # here ith time means you fired i+1 shot. if the number of monster exceed the number of shot, we have to return i
            if haveToKill[i]>i: return i
        
        return len(dist)
