---
tags:
  - math/linear_algebra/vector_spaces
---
### Idea
#### Column Space
^column-space
![[Pasted image 20250601162504.png]] ^3377da
#### Linear transformation
![[Pasted image 20250601163055.png]]
Here we can see that the output $b$ of $Ax = b$ will always lie inside the [[Span]] of $A$.
![[Pasted image 20250601163116.png]]
The Column Space of a matrix is affected by [[Gaussian Elimination]]
#### Row Space
![[Pasted image 20250601163433.png]]
The row space of a matrix is unaffected by [[Gaussian Elimination]].

#### Null Space
![[Pasted image 20250601163750.png]]
To see why Row space is perpendicular to Null space
![[Matrix multiplication#^e69113]]
Consider $Ax = 0$, by Mv1, we need $x$ [[Dot product|dot]] each row of $A$ to be 0, where $x$ is the Null space. 
##### Constructing Null Space
#status/todo
![[IMG_0688.jpeg]]
0![[Pasted image 20250601165411.png]]
Think of this like for $Ax = b$ as a function, we must have every single possible point within the row space to be mapped to a single point in the range, that means they have equal dimensions.

![[Pasted image 20250601165349.png]]

![[Pasted image 20250601171726.png|400]]
