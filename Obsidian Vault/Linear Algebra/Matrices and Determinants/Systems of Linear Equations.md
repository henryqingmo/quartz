### Idea
![[Pasted image 20250527145552.png]]
There are two ways of picturing solving linear equations. 
#### Row Picture
![[Pasted image 20250527145633.png|600]]
The row picture involves graphing the equations of each row, and finding their intersection. 

We think of solving the simultaneous equations, or equivalently the intersections of hyperplanes. 

#### Example
#status/todo 
In 2D, the hyperplane is a line.
![[Line#Idea]]
Solving the equations in 2D is like finding the intersection of lines. 
![[Assets/Pictures/MATH1131-1141-Algebra-Notes-2020T1 9.png]]
[[MATH1131-1141-Algebra-Notes-2020T1.pdf#page=142&rect=44,393,529,631|MATH1131-1141-Algebra-Notes-2020T1, p.132]]
Here we have 3 cases 

1.
No equations/constraints 
The entire plane is the solution. 

2.
1 constraints, result is a line.  eg. 
ax + by = c (not all a, b can be 0)

3.

2 constraints (2 linearly independent row), two lines intersecting in a plane is a point. 

![[Plane#Cartesian form]]

In 3D, the hyperplane is a plane. we have 1 condition for a plane, 2 for a line and 3 for a point. 
![[Assets/Pictures/MATH1131-1141-Algebra-Notes-2020T1 8.png]]
[[MATH1131-1141-Algebra-Notes-2020T1.pdf#page=142&rect=45,93,529,394|MATH1131-1141-Algebra-Notes-2020T1, p.132]]


The $b$ on the right hand side tells us if the line or plane passes through the origin.
We can clearly see that the intersection only at origin if all of these line/planes passes through the origin, which is the null space. 
#### Column Picture
![[Pasted image 20250527145936.png|600]]
The column picture involves finding the linear combinations of the two vectors that adds to the result.

We can represent each point as the linear combinations of standard basis. 


#### Practice Problem
![[Pasted image 20250527152251.png|500]]

#### Example
![[Pasted image 20250601172721.png|400]]
We can first check for the the column space, and see if $b$ lies there, but we can first perform [[Gaussian Elimination]] since it preserves the linear dependency of the columns.
![[Pasted image 20250601173233.png]]
The 2 pivot columns means the column space is of dimension 2. 
Since $\vec{b}$ exists within the column space, the 1 restriction imposed makes it a line. 
![[Pasted image 20250601173552.png]]
We can construct the NULL space, and add it to a particular solution.

The whole of the input space is the direct sum of the null space and the column space, here we have all the solutions for all the possible b, (a lines on the row space that can be extended by null space into a plane), so for a particular b value, the solution would be the null space shifted by a value on the particular solutions.

![[Pasted image 20250601174101.png]]

#math #linear_algebra 


