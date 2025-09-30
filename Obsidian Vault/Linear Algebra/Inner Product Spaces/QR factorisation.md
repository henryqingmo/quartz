---
tags:
  - math/linear_algebra
---
### Idea
![[Assets/Pictures/The-Art-of-Linear-Algebra 6.png]]
[[The-Art-of-Linear-Algebra.pdf#page=10&rect=62,255,517,759|The-Art-of-Linear-Algebra, p.10]]
> [!abstract]
We are basically reversing [[Gram-Schmidt]], each $a$ can be composed as it's component in all of the direction. We simply add up the unit vector scaled by length of it's projection of each direction.  
> >[!note]
> >If we consider reversing to get $a_2$, we first multiply both sides by $||q_2||$ which is exactly $<a_2, q_2>$ or $r_{22}$

![[IMG_1043.jpeg]]

![[Pasted image 20250925154552.png]]

![[Pasted image 20250925154614.png]]
> [!note]
> This exactly comes from the [[Linear Algebra/Linear Transformations/Projection|Projection]], where we have $Q$ in place of $A$

![[Pasted image 20250925154901.png]]
[[Pseudo Inverse]]

### Formally




