# Python3 program to check if
# a point lies inside a circle
# or not
import math
def isInside(circle_x, circle_y, rad, x, y):

	# Compare radius of circle
	# with distance of its center
	# from given point
	if ((x - circle_x) * (x - circle_x) +
		(y - circle_y) * (y - circle_y) <= rad * rad):
		return True;
	else:
		return False;

# Driver Code
x = 1;
y = 2;
circle_x = 0;
circle_y = 0;
circle_x1 = 0;
circle_y1 = 2;
rad = math.sqrt((circle_x-circle_x1)**2+(circle_y-circle_y1)**2)
print(rad)
if(isInside(circle_x, circle_y, rad, x, y)):
	print("Inside");
else:
	print("Outside");

# This code is contributed
# by mits.
