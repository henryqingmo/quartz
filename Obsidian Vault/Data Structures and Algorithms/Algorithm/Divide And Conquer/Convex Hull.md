---
tags:
  - coding/algorithm
---
### Idea
![[Pasted image 20251104151807.png|400]]
The problem is to find the line segments of the "gift wrap" The key thing to observe here is we can try to draw a line between each pair of points and see if it segregates all the points to one side. If it does, than it's a part of the wrap. 

![[Pasted image 20251104152344.png]]
We can first divide into two subproblems by drawing a line that separates the points into roughly equal sizes, We can then naively computes the convex hull when the size is small enough. 
Then we need to merge the two convex hull, we can do this by finding the maximum tangent and minimum tangent, with end points in both hulls. 

![[Pasted image 20251104153740.png]]
After with find the Upper and lower tangent, we need to use the cut and paste method, starting from the upper tangent, we follow it to the right hull, and traverse in the clock wise direction left hull and traverse counter clockwise until we reach to the upper tangent.  This exactly corresponds to us traversing along the outer of the new hull. 


