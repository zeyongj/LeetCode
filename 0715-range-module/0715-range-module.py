from bisect import bisect_left as bl, bisect_right as br
class RangeModule:


    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        arr = self.ranges
        i, j = bl(arr, left) , br(arr, right)
        resRange = []
        if i%2==0 : 
            resRange.append(left)
        if j%2==0 : 
            resRange.append(right)
        arr[i:j] = resRange

    ## Changed queryRange acc to my understanding :)
    def queryRange(self, left: int, right: int) -> bool:
        arr = self.ranges
        # NOTE here itss Bisect_Right for left , think...
        i = br(arr, left)
        if i < len(arr) and arr[i] >= right and i%2 == 1 :
            return True

        return False
        

    def removeRange(self, left: int, right: int) -> None:
        arr = self.ranges
        i, j = bl(arr, left) , br(arr, right)
        resRange = []
        if i%2==1 : 
            resRange.append(left)
        if j%2==1 : 
            resRange.append(right)
        arr[i:j] = resRange

        
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)