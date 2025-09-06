---
tags:
  - math/linear_algebra/matrix
---
### Idea
![[Pasted image 20250817213044.png]]

![[Pasted image 20250817230151.png]]
>[!note]
>Intuitively it make sense, the sum of the block size will be equal to the total number of [[Eigenvalues and eigenvectors|repeated eigenvalues]] , the number of block is the number of independent eigenvectors.
[[Eigenspace]]
#### Motivation

![[Pasted image 20250817012414.png]]
>[!note]
>When we have repeated eigenvalues, therefore we don't have enough linearly independent eigenvectors. 

![[Pasted image 20250817012801.png]]
>[!note]
>The solution would be instead of using the diagonal matrix, to introduce 1s on the super diagonal, this is call the jordon matrix. 

![[Pasted image 20250817013844.png]]
Now compare each columns.

![[Pasted image 20250817014005.png]]
>[!note]
>The first is a standard [[Eigenvalues and eigenvectors]]. 
>The second one has a component in $v_1$, so $(A-\lambda I)v_2$ now gives us $v_1$, the first eigenvector. For $v_3$, we apply once to get back to $v_2$.

![[Pasted image 20250817130800.png]]
We find $v_2$ by solving this equation.

![[Pasted image 20250817130927.png]]



