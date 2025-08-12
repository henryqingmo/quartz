---
tags:
  - math/linear_algebra
---

### Idea
![[Pasted image 20250720121907.png]]
Any linear function that maps from a [[Vector space]] $V$  to a [[Field]] $\mathbb{F}$ is inside the dual space. 

The dual space and vector is [[Morphism|Isomorphic]]. This can be proved using their dimension. 
![[Pasted image 20250720122240.png]]
The dimension of $V^*$ can be thought of as a matrix, with dimension of the domain multiplied by it's co domain.  Since the dual space and the vector have the same dimension, they are isomorphic.
> [!tip] 
> Intuitively, We are looking for every functional $f$ is an arrow that eats a vector and spits out a scalar.
> that can be seem as the bijective mapping of domain and range, which has at most dimension $V$, and there is exactly dim($V$) vectors in $V$.

#### Riesz representation theorem
![[Assets/Pictures/LADR.png]]
[[LADR.pdf#page=223&rect=14,283,355,387|LADR, p.205]]
> [!note]
> For every functional $\phi$ that maps from a [[Vector space]] to a [[Field]], we can represent uniquely with an [[Linear Algebra/Inner Product Spaces/Inner Product|Inner Product]] of the input vector and another vector from that vector field. That function is called the dual of that vector.
#### Proof
![[Assets/Pictures/LADR 1.png]]
[[LADR.pdf#page=223&rect=15,23,359,284|LADR, p.205]]
> [!abstract]
>1. we basically used [[Linear Algebra/Inner Product Spaces/Projection|Projection]] formula to rewrite $u$ in terms of it's component in each basis.
  2. We used the linearity property of $\phi$ and pulls out the constant
  >3. We can pull the constant into each of the inner product, and then that's the same as inner product of the whole thing. 




