# helper fxn for binary search
def binsear(arr, x):
    l=0
    r=len(arr)-1

    anstillnow=len(arr)
    # if we find no m such that arr[m]>=x, means that our x is greater than all values of length, in such case we return idx n (i.e. size of arr)
    # reason being, we substract our idx by size of arr to get number of rectangles greater than that in main fxn, so return arr.size would give us 0 (which we want)

    while(l<=r):
        m= l + (r-l)//2


        if(arr[m]>=x):
            anstillnow=m
            r=m-1;

        else:
            l=m+1

    return anstillnow

    
class Solution:

    def countRectangles(self, rect: List[List[int]], points: List[List[int]]) -> List[int]:
        
        # create a dictionary of int -> list of int
        htl=defaultdict(list)
        
        # maps heights to all the lengths of rectangles with that height
        for l, h in rect:       
            htl[h].append(l)
        
		# have to sort the containers to apply binary search
        for k,v in htl.items():
            v.sort()
        
		
        ans=[];
		
        for p in points:
            x=p[0]
            y=p[1]
            
            ct=0
            
            for j in range(y, 101):
                if j in htl:
                    ct+= len(htl[j]) - binsear(htl[j], x)
                    
					# binary search return the idx in array from which the values are >= x
					# the values at this and right of this are the lengths possible
					# so substract by size of array to get the number
            
            ans.append(ct)
        
        return ans