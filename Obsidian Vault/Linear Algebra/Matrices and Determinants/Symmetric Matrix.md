### Idea
#### A symmetrical matrix has the property
$$
A = A^{T} 
$$
This means that swapping elements along the main diagonal doesn't change the matrix, 
hence elements have to be the symmetric along the main diagonal.

### A skew symmetrical matrix has the property 
$$
-A = A^T
$$
This means that the main diagonal has to be all zero since after swap, 
the diagonal are the same. 
The element symmetric along the main diagonal has to be negative of each other. 
### proving symmetric 
$$
\begin{align*}
(AA^{T})^{T} &= AA^{T}\\
(A + A^{T})^{T}&= A^{T} + A
\end{align*}
$$
### Proving skew symmetric
$$
(A - A^{T})^{T} = A^{T} - A
$$

Symmetric matrices have orthogonal [[Eigenvalues and eigenvectors|eigenvectors]].
#### Decomposition
![[Pasted image 20250729114644.png|500]]
So it can be rewritten in this form.

![[Assets/Pictures/The-Art-of-Linear-Algebra 7.png]]
[[The-Art-of-Linear-Algebra.pdf#page=11&rect=64,395,561,779|The-Art-of-Linear-Algebra, p.11]]
> [!note]
> All symmetric matrix will have $A^{T}A= AA^{T}$, therefore is a special case of [[Normal Maps]], thus we can apply the [[Spectral Theorem]].

#math #linear_algebra 



