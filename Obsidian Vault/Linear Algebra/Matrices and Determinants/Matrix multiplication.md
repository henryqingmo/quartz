### Idea
![[Assets/Pictures/The-Art-of-Linear-Algebra 2.png]]
[[The-Art-of-Linear-Algebra.pdf#page=2&rect=59,451,551,797|The-Art-of-Linear-Algebra, p.2]]
It would be helpful to think of matrix as collections of row/column vectors, which is useful in matrix matrix mutiplication.

#### Vector and vector
![[Assets/Pictures/The-Art-of-Linear-Algebra 4.png]]
[[The-Art-of-Linear-Algebra.pdf#page=2&rect=65,155,534,322|The-Art-of-Linear-Algebra, p.2]]
[[Dot product]]
#### Matrix and vector
![[Assets/Pictures/The-Art-of-Linear-Algebra.png]]
[[The-Art-of-Linear-Algebra.pdf#page=3&rect=64,529,547,767|The-Art-of-Linear-Algebra, p.3]]

For `Mv1` we use dot product, for `Mv2`, we distributes it into linear combinations of columns, we will have the row space instead, if the matrix was on the right. 

![[Assets/Pictures/The-Art-of-Linear-Algebra 1.png]]
[[The-Art-of-Linear-Algebra.pdf#page=3&rect=76,229,510,456|The-Art-of-Linear-Algebra, p.3]]
For distribution, combination of column if matrix is on the left, combination of columns if matrix is on the right.

#### Matrix and Matrix
![[Assets/Pictures/The-Art-of-Linear-Algebra 3.png]]
[[The-Art-of-Linear-Algebra.pdf#page=5&rect=82,526,521,796|The-Art-of-Linear-Algebra, p.5]]
We can think of matrix as collections of vector, which we can apply matrix to.

For the top `MM1`, we used [[Dot product]]. 
For `MM2` we separate the right matrix into columns, and applied matrix to each column. 
For `MM3` swapped the order of `MM2`, and apply right matrix to each column of the left
For `MM4` we used `V2`


![[Assets/Pictures/The-Art-of-Linear-Algebra 5.png]]
[[The-Art-of-Linear-Algebra.pdf#page=5&rect=61,156,552,463|The-Art-of-Linear-Algebra, p.5]]
For `P1` we basically apply matrix to each row `MM2` and then turned each multiplication of column into linear combination of columns using `Mv2`

For `P2` we do applied the matrix to each row `MM3` and expand using `vM2`

Here is an video showing `P1`
![[Visualizing Matrix Multiplication - YouTube.mp4]]

#math #algebra #linear_algebra 



