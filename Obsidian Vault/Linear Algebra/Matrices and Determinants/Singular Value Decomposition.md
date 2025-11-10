---
tags:
  - math/linear_algebra/matrix
---

### Idea
![[Pasted image 20251006021052.png|500]]
We basically want to find a pair of orthogonal vectors that remains orthogonal after the transformation.


![[Pasted image 20250729125245.png]]
>[!note]
>The V matrix is composed with basis of row space and [[The Four Fundamental Subspaces#Null Space|NullSpace]], because how their eigenvalues are arranged from largest all the way to 0, where eigenvectors of $\lambda = 0$ corresponds to the kernel.

#### Reduced SVD
![[Pasted image 20250807172345.png]]
>[!note]
>For reduced SVD, we basically utilised the fact that some of the eigenvalues are 0, so we truncate the matrix into a invertible full ranked matrix.


![[Assets/Pictures/The-Art-of-Linear-Algebra 8.png]]
[[The-Art-of-Linear-Algebra.pdf#page=11&rect=64,93,563,397|The-Art-of-Linear-Algebra, p.11]]



