class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
		# Getting the coords of centre of rectangle
        c1 = (x2 + x1) / 2
        c2 = (y2 + y1) / 2
        
		# Getting distance between centre of circle and rectangle in x, y direction
		# Abs for suppose centre of circle in 3rd quad and of rectangle in 1st quad
        v1 = abs(x_center - c1) 
        v2 = abs(y_center - c2)
        
		# Getting half of breadth and lenght of rectangle
        h1 = (x2 - x1) / 2 
        h2 = (y2 - y1) / 2
         
		# Difference in distance between (i) half of side of rectangle (h1,h2) (ii) distance between circle and rectangle
		# It can be negative For eg. If circle is completely in rectangle. Hence taking max with zero
        u1 = max(0, v1 - h1)
        u2 = max(0, v2 - h2)
        
		# Now try to think yourself for this last step
		# Hint is hypotenuse !!
        return (u1 * u1 + u2 * u2 <= radius * radius)

        # Hope you get it :)
