### Idea
![[Assets/Pictures/chap3_LinSys 20.png]]
[[chap3_LinSys.pdf#page=12&rect=65,211,526,479|chap3_LinSys, p.12]]

Here we utilised ![[Triangular Matrix#Lower Triangular matrix]]
The diagonals should be all 1s, considering it's a product of [[Elementary Row Operations#Elementary Matrix|Elementary Matrix]].

![[Triangular Matrix#Upper triangular matrix]]
The Upper triangular matrix can have 0s on the diagonals.

#### Example
![[Assets/Pictures/chap3_LinSys 21.png]]
[[chap3_LinSys.pdf#page=12&rect=65,48,528,213|chap3_LinSys, p.12]]

![[Assets/Pictures/chap3_LinSys 22.png]]
[[chap3_LinSys.pdf#page=13&rect=78,390,522,694|chap3_LinSys, p.13]]

The Upper [[Triangular Matrix]] is exactly the result of [[Gaussian Elimination]] if $A$ is a square  matrix.
![[Assets/Pictures/chap3_LinSys 23.png]]
[[chap3_LinSys.pdf#page=13&rect=77,49,523,392|chap3_LinSys, p.13]]

![[Pasted image 20250520144916.png]]



![[Assets/Pictures/chap3_LinSys 24.png]]
[[chap3_LinSys.pdf#page=14&rect=63,510,529,696|chap3_LinSys, p.14]]

In this example we cannot proceed without swapping row 2 with row 3, which is not allowed in the standard decomposition.

This is because of this theorem
![[Assets/Pictures/chap3_LinSys 26.png]]
[[chap3_LinSys.pdf#page=14&rect=65,162,525,308|chap3_LinSys, p.14]]

The [[Principal Submatrix]] $A_2$ is singular.

![[Assets/Pictures/chap3_LinSys 27.png]]
[[chap3_LinSys.pdf#page=14&rect=66,62,526,167|chap3_LinSys, p.14]]
$A_{1}$ and $A_2$ are both non-singular.

####  Pivoting 
We have to introduce Pivoting to account for this. 
![[Assets/Pictures/chap3_LinSys 29.png]]
[[chap3_LinSys.pdf#page=15&rect=79,319,526,531|chap3_LinSys, p.15]]
However the swapping of rows introduce a [[Permutation Matrix]] 

####  Computation Cost
##### Upper Triangle
![[Assets/Pictures/chap3_LinSys 30.png]]
[[chap3_LinSys.pdf#page=25&rect=65,66,537,558|chap3_LinSys, p.25]]

We first find the elimination factors, with pivots of each row(excluding the first row) divides the first row, which is (n - 1) divisions. 

By considering updating the elements that's gonna be 0, for each element, we have 1 division, 1 multiplication and 1 subtraction, for a total of **$n-1$ elements**, giving us **$3(n-1)$ operations**. 

The lecture **doesn't** account for the updating of 0s for the large matrix. It only looks at updating the submatrix, which would have $(n-1)^2$ elements. 

![[Assets/Pictures/chap3_LinSys 31.png]]
[[chap3_LinSys.pdf#page=26&rect=71,410,530,692|chap3_LinSys, p.26]]
[[Numerical Analysis/Float/Big O Notation|Big O Notation]]
##### Lower Triangle
![[Assets/Pictures/chap3_LinSys 33.png]]
[[chap3_LinSys.pdf#page=26&rect=70,52,530,413|chap3_LinSys, p.26]]

#math #coding #linear_algebra 



