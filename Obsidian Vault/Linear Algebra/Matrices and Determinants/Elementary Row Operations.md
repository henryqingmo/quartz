### Idea

There are three Elementary Row Operations, which can be represented with 3 types of matrices. 

$AB$ can be represented as A encoding the linear combinations of rows of B, which make it possible to represent any Elementary Row Operation. 

![[Matrix multiplication#Further Decomposition]]

#### Identity Matrix
![[Assets/Pictures/Lecture notes 2.png]]
[[Lecture notes.pdf#page=10&rect=62,62,547,148|Lecture notes, p.10]]

$IA$ represent having 1 of each row adding to 0 of other rows, which does nothing to each row. 

#### Elementary Matrix
![[Assets/Pictures/Lecture notes.png]]
[[Lecture notes.pdf#page=7&rect=72,582,557,738|Lecture notes, p.7]]

We will have 1 on the diagonal to denote 1 of each row, and $\lambda$ at $E_{ij}$ to denote the addition of $\lambda \;\text{row(j) to row(i)}$ 

#### Permutation Matrix
![[Assets/Pictures/Lecture notes 1.png]]
[[Lecture notes.pdf#page=7&rect=73,421,557,584|Lecture notes, p.7]]

To represent the swapping of rows, we just swapped the [[Elementary Row Operations#Identity Matrix|Identity Matrix]].

There will be $n!$ possible Permutation for $n$ rows, and $P^{-1} = P^{T}$.

#### Diagonal Matrix
Diagonal matrix have 0 outside the diagonals, and any values(including 0s) on principal diagonal. 
![[Assets/Pictures/Lecture notes 3.png]]
[[Lecture notes.pdf#page=7&rect=74,249,557,420|Lecture notes, p.7]]

We use the diagonal Matrix to scale a specific row



#math #linear_algebra 



