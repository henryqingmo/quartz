---
tags:
  - math/linear_algebra/matrix
---
### Idea
![[Pasted image 20250807174004.png|500]]
> [!note]
> In the case where the input less than output, we will either get 0 or 1 solution, depends if $b$ lies inside or outside column space of $A$.
> 
> If the rank is exactly the number of column, the all of the input is mapped to a subspace of the output, and $A^TA$ is invertible.


![[Pasted image 20250807174602.png|500]]
>[!note]
For the left inverse, we have input less than output, which means we can 

#### Pseudo Inverse
![[Pasted image 20250807175612.png|500]]
> [!note]
> The idea behind pseudo Inverse is that the mapping from the row space to the column space has to be one-to-one, therefore invertible, if we restrict only to that space. 
> ![[Pasted image 20250807175940.png]]

![[Assets/Pictures/Handout 6.3 - Geometric properties and singular value decomposition.png]]
[[Handout 6.3 - Geometric properties and singular value decomposition.pdf#page=14&rect=17,49,348,248|Handout 6.3 - Geometric properties and singular value decomposition, p.13]]

![[Pasted image 20250811232826.png]]
The [[Linear Algebra/Linear Transformations/Projection|Projection]] [[Linear Algebra/Inner Product Spaces/Projection|Projection]] Matrix is exactly composed with the column space basis with the [[Singular Value Decomposition#Reduced SVD|Reduced SVD]].


### Formally




